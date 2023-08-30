import os

from dotenv import load_dotenv
import praw

load_dotenv()

reddit = praw.Reddit(
    client_id= os.getenv('API_KEY'),
    client_secret= os.getenv('SECRET'),
    password= os.getenv('REDDIT_PWD'),
    user_agent= "SentimentPipelineAWS v1.0 by u/notdanke1337",
    username= os.getenv('REDDIT_USR'),
)



#curl command example
# headers = {"Authorization": f"bearer {os.getenv('TOKEN')}", "User-Agent": "SentimentPipelineAWS v1.0 by /u/notdanke1337"}
# response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
# print(response.json())


