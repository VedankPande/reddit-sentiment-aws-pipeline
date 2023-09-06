import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Compatibility for lambda
lambda_nltk_data_path = '/tmp/nltk_data'
if lambda_nltk_data_path not in nltk.data.path:
    nltk.data.path.append(lambda_nltk_data_path)
    
nltk.download('vader_lexicon', download_dir= lambda_nltk_data_path)

def get_sentiment_dict(text: str) -> dict:
    
    sent_analyzer = SentimentIntensityAnalyzer()
    sent_dict = sent_analyzer.polarity_scores(text)
    return sent_dict