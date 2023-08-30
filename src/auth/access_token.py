import requests
import dotenv
import os

dotenv.load_dotenv()

def refresh_token():
    
    '''
    refresh the token in environment variables
    '''

    dotenv_path = "C:/Users/vedan/Desktop/code/aws-reddit-sent/.env"

    data = {
        'grant_type': 'password',
        'username': os.getenv('REDDIT_USR'),
        'password': os.getenv('REDDIT_PWD'),
    }

    response = requests.post(
        'https://www.reddit.com/api/v1/access_token',
        data=data,
        auth=(os.getenv('API_KEY'), os.getenv('SECRET')),
    )

    dotenv.set_key(dotenv_path, "TOKEN", response.text["access_token"])