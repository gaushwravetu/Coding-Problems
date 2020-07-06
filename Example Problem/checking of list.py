class node:
    def __init__(self,initial=None):
        self.value = initial
        self.next = None
    def isempty(self):
        return(self.value == None)
