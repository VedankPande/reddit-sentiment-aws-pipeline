# Twitter Sentiment Analysis Pipeline

Optional treelib code changes for development:

 1. tree.py -> `show` function (line 870): Printing a tree outputs the Tree object in byte format. If you have this problem as well, change `print(self.reader.encode('utf-8'))` to `print(self.reader)`. Only needed if you want a tree structure display of your comments tree. Source: [This stackoverflow post](https://stackoverflow.com/questions/46345677/treelib-prints-garbage-instead-of-pseudographics-in-python3)


## Architecture:

![Alt text](/media/architecture.png "Optional title")