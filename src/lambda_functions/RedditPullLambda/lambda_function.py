import json
import os
import base64
import pickle

import boto3
import praw

from scrapers.postScraper import PostScraper
from scrapers.commentScraper import CommentScraper
from utilities.logger import enable_praw_logging
from utilities.treeUtils import CommentTree

enable_praw_logging()

reddit = praw.Reddit(
    client_id= os.environ['API_KEY'],
    client_secret= os.environ['SECRET'],
    password= os.environ['REDDIT_PWD'],
    user_agent= "SentimentPipelineAWS v1.0",
    username= os.environ['REDDIT_USR'],
)

ps = PostScraper(reddit)
cs = CommentScraper(reddit)
treegen = CommentTree()
sqs = boto3.client('sqs')

sqs_url = "https://sqs.ap-south-1.amazonaws.com/530128583111/ComprehendLambdaQueue"

def lambda_handler(event, context):
    

    subreddit = "FantasyPL"
    keywords = "Rashford"
    num_posts = 1
    posts = ps.get_submissions(subreddit, keywords, limit=num_posts) 
    
    for post in posts:

        comments = cs.get_comments(post, recursive = True)
        tree = treegen.generateTree(comments, root_data = {"subreddit":subreddit, "keywords":keywords, "post_id": post.id, "num_posts":num_posts})
        tree.show()
        
        message_body = str(base64.b64encode(pickle.dumps(tree)), encoding='utf-8')
        
        response = sqs.send_message(
            QueueUrl = sqs_url,
            MessageBody = message_body,
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Pulled all the required data and sent it to SQS for further processing!')
    }