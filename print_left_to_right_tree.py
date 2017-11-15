'''Print nodes from left to right in a tree

            1
        2       3
    4       5       6
    >>> Tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))
    >>> Tree.print_left_to_right()
    4
    2
    5
    1
    3
    6

        
            3
        2
    1
    >>> Tree1 = Node(3, Node(2, Node(1)))
    >>> Tree1.print_left_to_right()
    1
    2
    3

            4
                3   
                    2

    >>> Tree2 = Node(4, None, Node(3, None, Node(2)))
    >>> Tree2.print_left_to_right()
    4
    3
    2

'''
class Node(object):
    '''Node in a tree'''

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_left_to_right(self):

        def _print(node):
            if node == None:
                return
            
            _print(node.left)
            print node.data
            _print(node.right)

        return _print(self)

 
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
    
