from praw import Reddit



class BaseScraper:
    """
    Superclass to implement various scrapers over the Reddit API
    """
    def __init__(self,reddit: Reddit) -> None:
        
        self.reddit = reddit
        self._last_accessed = ""
    
    @property
    def last_accessed(self) -> str:

        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, value) -> None:
        if not isinstance(value,str):
            raise TypeError("Last accessed must be a string")
        self._last_accessed = value

    



