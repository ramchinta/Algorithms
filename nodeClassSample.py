class node:
    def __init__(self,data):
        self.data = data
        self.next = None
'''The next pointer is initialized to None, meaning that unless you change the value of next,
 the node is going to be an end-point. This is a good idea, so that we do not forget to terminate the list properly.'''