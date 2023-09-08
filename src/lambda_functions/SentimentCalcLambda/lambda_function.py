import json
import treelib
import pickle
import base64
import boto3
import requests
from requests_aws4auth import AWS4Auth

from sentiment.submissionSentiment import SubmissionSentiment
from math import copysign


region = 'ap-south-1' 
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://search-elasticredditsentiment-cilnjwunulmc6nke43xogssrmu.ap-south-1.es.amazonaws.com'
index = 'lambda-reddit-sentiment'
datatype = '_doc/'
url = host + '/' + index + '/' + datatype

headers = { "Content-Type": "application/json" }

def lambda_handler(event, context):
    decoded = base64.b64decode(event["Records"][0]["body"])
    tree = pickle.loads(decoded)
    
    print(tree)
    score = SubmissionSentiment(tree).calculate_tree_sentiment()
    print(f"Sentiment score for this submission: {score}")
    
    document = {"Sentiment": score}
    
    r = requests.post(url, auth=awsauth, json=document, headers=headers)
    print(r.text)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
