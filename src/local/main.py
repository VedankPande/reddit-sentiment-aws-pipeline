import os
import base64
import pickle

#third party imports
from dotenv import load_dotenv
import praw
import nltk

#local imports
from scrapers.postScraper import PostScraper
from scrapers.commentScraper import CommentScraper
from utilities.logger import enable_praw_logging
from utilities.treeUtils import CommentTree
from sentiment.submissionSentiment import SubmissionSentiment
#environment setup
enable_praw_logging()
load_dotenv()

reddit = praw.Reddit(
    client_id= os.getenv('API_KEY'),
    client_secret= os.getenv('SECRET'),
    password= os.getenv('REDDIT_PWD'),
    user_agent= "SentimentPipelineAWS v1.0",
    username= os.getenv('REDDIT_USR'),
)

if __name__ == "__main__":

    ps = PostScraper(reddit)
    cs = CommentScraper(reddit)
    treegen = CommentTree()
    posts = ps.get_submissions("FantasyPL","Haaland",limit=1) 
    
    for post in posts:

        comments = cs.get_comments(post, recursive = True)
        tree = treegen.generateTree(comments)
        tree.show()
        
        print(f"Sentiment score for this submission: {SubmissionSentiment(tree).calculate_tree_sentiment()}")