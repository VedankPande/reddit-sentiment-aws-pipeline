from praw import Reddit



class BaseScraper:
    """
    Superclass to implement various scrapers over the Reddit API
    """
    def __init__(self,reddit: Reddit) -> None:
        
        self.reddit = reddit
    



