"""
module to calculate sentiment for a given tree of comments
"""

import treelib

# Maybe you can add all these methods to a custom tree class instead?
class SubmissionSentiment:
    """
    class to calculate sentiment for a given tree
    """
    def __init__(self, commentTree) -> None:

        self.commentTree = commentTree
        

    def get_node_sentiment(self, node: treelib.Node, parent: treelib.Node, comprehendClient) -> int:
        """
        calculate sentiment for a node (comment) in the tree 
        """

        raw_score = comprehendClient(node.data.comment)

        #TODO: adjust score for parent polarity and current nodes reddit score (upvote - downvote)
        adjusted_score = None

        return adjusted_score


    def get_parent_node(self,node: treelib.Node) -> treelib.Node:
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
        
        #TODO: get boto3 comprehend client here
        comprehend = None
        submission_score = 0

        for node in self.commentTree.expand_tree():

            #root node
            if type(node) == str:
                continue

            parent = self.get_parent_node(node, self.commentTree)

            node_score = self.get_node_sentiment(node, parent, comprehend)

            #update nodes score and submission score
            node.data.score = node_score
            submission_score += node_score



















