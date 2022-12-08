class Node(object):
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
