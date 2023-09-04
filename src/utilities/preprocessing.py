"""
Preprocess comments to obtain accurate results from comprehend
"""

import emoji
import regex as re

def clean_tweet(comment)->str:
    '''
    Removes links and special characters from text
    '''
    
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", comment).split()) 

def clean_emojis(comment):
    """
    remove or replace emojis with corresponding text
    """
    return emoji.demojize(comment,delimiters=("",""))
