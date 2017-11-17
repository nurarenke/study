""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    
    def _bst_validator(root, low=-1, high=10001):
        if root == None:
            return True
        
        if not (root.data < high and root.data > low):
            return False

        if root.left is not None and root.left.data >= root.data:
            return False

        if root.right is not None and root.right.data <= root.data:
            return False
        
        left = _bst_validator(root.left, low, root.data)
        right = _bst_validator(root.right, root.data, high)

        return left and right

    return _bst_validator(root)