import os

import praw
import dotenv
from praw import Reddit



class CommentScraper:
    
    """
    Class to retrieve  comments for a given submission (post)
    """
    def __init__(self,reddit: Reddit) -> None:
        self.reddit = reddit
        self._last_accessed = None

    @property
    def last_accessed(self) -> str:

        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, value) -> None:
        if not isinstance(value,str):
            raise TypeError("Last accessed must be a string")
        self._last_accessed = value
    

    def get_comments(self,submission: Reddit.submission):
        """
        Returns a 
        """
        pass



    
    


