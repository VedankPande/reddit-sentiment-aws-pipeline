import os

#third party imports
from dotenv import load_dotenv
import praw
from praw.models.reddit.more import MoreComments

#local imports
from scrapers.postScraper import PostScraper
from scrapers.commentScraper import CommentScraper
from utilities.logger import enable_praw_logging
from utilities.treeUtils import CommentTree
#environment setup
enable_praw_logging()
load_dotenv()

reddit = praw.Reddit(
    client_id= os.getenv('API_KEY'),
    client_secret= os.getenv('SECRET'),
    password= os.getenv('REDDIT_PWD'),
    user_agent= "SentimentPipelineAWS v1.0 by u/notdanke1337",
    username= os.getenv('REDDIT_USR'),
)

if __name__ == "__main__":

    ps = PostScraper(reddit)
    cs = CommentScraper(reddit)
    treegen = CommentTree()
    posts = ps.get_submissions("FantasyPL","Everton") 
    
    for post in posts:
        pass

    
    dfs = treegen.getDepthFirstTraversal(post.comments)
    tree = treegen.generateTree(dfs)

    tree.show(data_property="comment")


