import os 

import praw

from .baseScraper import BaseScraper


class PostScraper(BaseScraper):
    """
    Class to retrieve posts from a subreddit 
    """
    def __init__(self, reddit: praw.Reddit) -> None:
        super().__init__(reddit)
    
    def get_submissions(self, subreddit: str, search_term: str, limit: int = 100):

        sub = self.reddit.subreddit(subreddit)

        posts = sub.search(
            query = search_term,
            sort = "hot",
            #time_filter = "week",
            limit = limit,
        )

        return posts