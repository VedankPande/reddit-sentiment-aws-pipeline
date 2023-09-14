import os
import json
import treelib
import pickle
import base64
import boto3
import requests
from requests_aws4auth import AWS4Auth

from sentiment.submissionSentiment import SubmissionSentiment
from utilities.dataUtils import get_current_time
from math import copysign

#constants
region = 'ap-south-1' 
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

#connection information
host = os.environ["OPENSEARCH_DOMAIN_URL"]
request_index = os.environ["OPENSEARCH_REQUEST_INDEX"]
sentiment_index = os.environ["OPENSEARCH_SENTIMENT_INDEX"]

datatype = '_doc/'
headers = { "Content-Type": "application/json" }
url = host + '/' + request_index + '/' + datatype

bulk_datatype = '_bulk/'
bulk_url = host + '/' + sentiment_index + '/' + bulk_datatype
bulk_headers = { "Content-Type": "application/x-ndjson" }

def lambda_handler(event, context):
    decoded = base64.b64decode(event["Records"][0]["body"])
    tree = pickle.loads(decoded)
    
    meta_data = tree.get_node("root").data
    
    request_data = {"request_id": context.aws_request_id ,"timestamp": get_current_time(),
                    "subreddit": meta_data["subreddit"],"keywords": meta_data["keywords"],
                    "num_posts": meta_data["num_posts"]}
    
    r = requests.post(url, auth=awsauth, json=request_data, headers=headers)
    print(r)
    
    payload = ""
                    
    for score in SubmissionSentiment(tree).tree_sentiment_generator():
        
        comment_sentiment_data = {"request_id": context.aws_request_id ,"submission_id": meta_data["post_id"], "timestamp":get_current_time(), **score}
        payload += '\n' + '{"index": {"_index":"lambda-reddit-sentiment"}}' + '\n' + json.dumps(comment_sentiment_data) + '\n'
    
    #(payload)
    #document = {"Sentiment": score}
    
    r = requests.post(bulk_url, auth=awsauth, data=payload, headers= bulk_headers)
    print(r.text)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
