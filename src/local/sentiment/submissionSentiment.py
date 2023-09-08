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

        parent = self.get_parent_node(node)
        parent_polarity = copysign(1,parent.data.sentiment)
        comment_sentiment = get_sentiment_dict(node.data.comment)["compound"]*node.data.score

        return comment_sentiment*parent_polarity


    def get_parent_node(self, node: treelib.Node) -> treelib.Node:
        """
        return the predecessor or parent of a node in the tree
        """

        return self.commentTree.get_node(node.predecessor(self.commentTree.identifier))


    def calculate_tree_sentiment(self):
        """
        Function to calculate sentiment for a provided tree consisting of comments.

        Args:
            - commentTree: A treelib Tree object containing comments and their replies for a particular post/submission
            - comprehendClient: A boto3 client for AWS Comprehend for running sentiment scoring tasks

        Return:
            - results: TODO:
        """
        
        submission_score = 0

        for node in self.commentTree.expand_tree():

            node = self.commentTree.get_node(node)
            if node.identifier == "root":
                continue
            node_score = self.get_node_sentiment(node)

            #update nodes score and submission score
            node.data.score = node_score
            submission_score += node_score

        return submission_score


















