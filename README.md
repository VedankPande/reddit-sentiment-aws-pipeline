# Twitter Sentiment Analysis Pipeline

## IMPORTANT:

Treelib library changes to run this code:
1. tree.py -> `expand_tree` function (line 417): Edit the generator to yield the node object instead of just returning the node identifier (string). To do this, set `yield queue[0].identifier` to `yield queue[0]` and `yield stack.pop(0).identifier` to `yield stack.pop(0)`.

    These changes make sure all non root nodes return a `treelib.node.Node` object instead of the node identifier (string). Alternatively you could use the default string identifier that `expand_tree` returns and use the `treelib.tree.get_node` method to get the node for each node identifier. 

 2. tree.py -> `show` function (line 870): This one's optional. Printing a node outputs the Node object in byte format. If you have this problem as well, change `print(self.reader.encode('utf-8'))` to `print(self.reader)`. Only needed if you want a tree structure display of your comments tree. Source: [This stackoverflow post](https://stackoverflow.com/questions/46345677/treelib-prints-garbage-instead-of-pseudographics-in-python3)
    