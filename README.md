# Reddit Sentiment Analysis Pipeline



## Architecture:

![Architecture](/media/architecture.png "Optional title")

## Folder structure:
- lambda_functions: Code to deploy to lambda functions
- lambda_layer: Python dependencies for the lambda layer
- local: modules for local development

## Features

- Serverless architecture
- Store and visualize sentiment for submissions

## Setup Instructions

## Important for AWS functionality
 - The Python runtime version on your AWS Lambda must be the same as the one used when installing libraries for the lambda layer. If you use the layer provided in `src/lambda_layer`, set the lambda runtime version to `3.9`
 - When running `nltk` on your lambda, you might face the following error: 
 `Unable to import module 'lambda_function': No module named 'regex._regex'`. This usually happens if you're developing locally on Windows. To fix, download the regex library wheel into your lambda layer directory with the command:

        pip install --platform manylinux2014_x86_64 --target=. --implementation cp --python-version 3.9 --only-binary=:all: --upgrade regex
    Note: You need to cd into the layer directory first (or put the full path to your lambda as the `target`) Source: [AWS Article](https://repost.aws/knowledge-center/lambda-python-package-compatible)



### Optional treelib code changes for development:

 1. tree.py -> `show` function (line 870): Printing a tree outputs the Tree object in byte format. If you have this problem as well, change `print(self.reader.encode('utf-8'))` to `print(self.reader)`. Only needed if you want a tree structure display of your comments tree. Source: [This stackoverflow post](https://stackoverflow.com/questions/46345677/treelib-prints-garbage-instead-of-pseudographics-in-python3)


### Lambda-Opensearch permissions:
  - Add `AmazonOpenSearchServiceFullAccess` policy to the sentiment lambda function
  - Map your lambda role to an OpenSearch user if you're using fine grained control: Steps: [AWS docs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/search-example.html)
