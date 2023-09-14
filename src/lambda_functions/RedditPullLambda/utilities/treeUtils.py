from treelib import Node,Tree
from praw.models.reddit.more import MoreComments

# Node(tag = "id",identifier = id, data = (comment,score))

class CommentData():
    """
    Class to store data that is stored in the tree nodes
    """
    def __init__(self,comment,score) -> None:
        self.comment = comment
        self.score = score
        self.sentiment = 0

class CommentTree:
    """
    Class to construct a tree for the comments on a submission/post
    """
    def __init__(self) -> None:
        pass

    def getDepthFirstTraversal(self, commentForest) -> list:
        """
        Get the depth first traversal of the comments in a submission/post

        Args:
         - commentForest: A PRAW CommentForest class object that contains comments for a particular post
        
        Return:
         - A list of comments in the depth first traversal order
        """
        tree = Tree()
        tree.create_node("Root","root")

        comments = []

        #add all current top level comments to the queue
        stack = list(commentForest)

        while stack:
            comment = stack.pop(0)
            comments.append(comment)

            #add to all replies to stack if it's not a MoreComments object
            if not isinstance(comment, MoreComments):
                stack[0:0] = comment.replies

        return comments

    def generateTree(self, comments, root_data = None)->Tree:
        """
        Generate a tree based on the dfs traversal of the comments in a submission/post

        Args: 
            - A list containing a depth first traversal of comments for a particular post
        
        Return:
            - A treelib Tree object that contains the comments of the provided dfs traversal in a tree format
        """
        tree = Tree()

        #root node
        tree.create_node("Root", "root", data = root_data)

        traversal = self.getDepthFirstTraversal(comments)
        for comment in traversal:

            parent_comment = comment.parent_id

            #comment.id does not include the prefix, but comment.parent_id does. Adding the prefix here to keep the id format in the tree consistent
            comment_id = "t1_" + comment.id

            #check for top-level comment and set parent as root if true
            if parent_comment[:2] == "t3":
                parent_comment  = "root"

            #create node with data payload
            tree.create_node(comment_id, comment_id, parent=parent_comment, data = CommentData(comment.body, comment.score))

        return tree






    

