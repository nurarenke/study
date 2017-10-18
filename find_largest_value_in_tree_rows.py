#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

'''
This problem is from Codefights:

You have a binary tree t. Your task is to find the largest value in each row of this tree. In a tree, a row is a set of nodes that have equal depth. 
For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

Return an array in which the first element is the largest value in the row 
with depth 0, the second element is the largest value in the row with depth 1, 
the third element is the largest element in the row with depth 2, etc.

    >>> t = {"value": -1, "left": { "value": 5, "left": None, "right": None }, "right": {"value": 7, "left": None, "right": { "value": 1, "left": None, "right": None }}}

    >>> largestValuesInTreeRows(t)
    [-1, 7, 1]
'''
def largestValuesInTreeRows(t):
    root = t
    maxes = []
    row = [root]
    while any(row):
        maxes.append(max(node["value"] for node in row))
        row = [kid for node in row for kid in (node["left"], node["right"]) if kid]
    return maxes
    

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"