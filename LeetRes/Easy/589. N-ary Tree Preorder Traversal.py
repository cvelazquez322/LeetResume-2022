"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def io(root, rlist):
    rlist.append(root.val)   
    if root.children:
        while root.children:
            io(root.children[0], rlist)
            del root.children[0]
    return rlist
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        return io(root, [])