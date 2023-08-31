import os


import dotenv
from praw import Reddit
from praw.models import Submission

from .baseScraper import BaseScraper

class CommentScraper(BaseScraper):
    
    """
    Class to retrieve  comments for a given submission (post)
    """
    def __init__(self, reddit: Reddit) -> None:
        super().__init__(reddit)

    def get_comments(self,submission: Submission, recursive: bool = False):
        """
        Returns a CommentForest for the submission.
        Optionally resolved the MoreComments in the forest

        Args:
         - submission: PRAW Reddit.submission object that contains submission data
         - recursive (bool): If true, the PRAW replace_more function is used to
           recursively get comments from MoreComments instances found in the top-
           level.

        Returns:
            A praw CommentsForest object that optionally has any MoreComments object
            resolved. 
        """

        if not isinstance(submission, Submission):
            raise ValueError("submission must be of type: praw.Reddit.submission")

        if not isinstance(recursive, bool):
            raise ValueError("recursive must be a Boolean")
        
        if recursive:
            submission.comments.replace_more(limit = None)
        
        return submission.comments

        
        




    
    


