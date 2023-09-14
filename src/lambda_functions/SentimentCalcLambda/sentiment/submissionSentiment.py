"""
module to calculate sentiment for a given tree of comments
"""

import treelib
from math import copysign
from .vaderSentiment import get_sentiment_dict

# Maybe you can add all these methods to a custom tree class instead?
class SubmissionSentiment:
    """
    class to calculate sentiment for a given tree
    """
    def __init__(self, commentTree) -> None:

        self.commentTree = commentTree

    def get_node_sentiment(self, node: treelib.Node) -> int:
        """
        calculate sentiment for a node (comment) in the tree 
        """
        return get_sentiment_dict(node.data.comment)
    

    def get_adjusted_node_sentiment(self, node: treelib.Node) -> dict:
        """
        Description: adjust raw comment sentiment score for factors like parent comment polarity and the current comments score (upvotes/downvotes)
        
        Args:
            - node (treelib.Node): Node from the comment tree containing a CommentData object
        
        Returns:
            - sentiment (dict): A dictionary containing sentiment results including adjusted sentiment for the node

        """

        parent = self.get_parent_node(node)
        parent_sentiment = 0 if parent.identifier == "root" else parent.data.sentiment
        parent_polarity = copysign(1, parent_sentiment)
        sentiment = self.get_node_sentiment(node)
        sentiment["adjusted_sentiment"] = sentiment["compound"]*node.data.score*parent_polarity

        return sentiment


    def get_parent_node(self, node: treelib.Node) -> treelib.Node:
        """
        return the predecessor or parent of a node in the tree
        """

        return self.commentTree.get_node(node.predecessor(self.commentTree.identifier))


    def tree_sentiment_generator(self):
        """
        Function to calculate sentiment for a provided tree consisting of comments.

        Args:
            - commentTree: A treelib Tree object containing comments and their replies for a particular post/submission
            - comprehendClient: A boto3 client for AWS Comprehend for running sentiment scoring tasks
        """

        submission_score = 0

        #expand_tree provides a dfs traversal of the tree and returns the string identifier for each node
        for node in self.commentTree.expand_tree():
            
            #get node object using the identifier
            node = self.commentTree.get_node(node)

            if node.identifier == "root":
                continue
            
            node_score = self.get_adjusted_node_sentiment(node)

            #update nodes score and submission score
            node.data.score = node_score["adjusted_sentiment"]
            submission_score += node_score["adjusted_sentiment"]

            yield {"comment_id":node.identifier, **node_score}


















