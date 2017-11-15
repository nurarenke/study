'''Print path that sums to the value in a given tree.
    From Cracking the coding interview, problem 4.9.

            1
        3           5
    2       6   9       4

    >>> Tree = Node(1, Node(3, Node(2), Node(6)), Node(5, Node(9), Node(4)))
    >>> Tree.print_sum_path(10)
    1
    3
    2

'''
class Node(object):
    '''Node in a tree'''

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_sum_path(self, value):

        def _DFS_print(node, value, visited=[]):

            if node == None:
                return

            if sum(visited) == value:
                return visited

            if node != None:
                visited.append(node.data)
                print "visited", visited

                _DFS_print(node.left, value, visited)
                _DFS_print(node.right, value, visited)

            return "No path found"
         

        return _DFS_print(self, value)

 
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"