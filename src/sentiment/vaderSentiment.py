import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#TODO: run only once - maybe store it in the layer and then upload?
nltk.download('vader_lexicon')

def get_sentiment_dict(text: str) -> dict:
    
    sent_analyzer = SentimentIntensityAnalyzer()
    sent_dict = sent_analyzer.polarity_scores(text)
    return sent_dict