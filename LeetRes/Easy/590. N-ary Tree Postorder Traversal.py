"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def po(root, rlist):
    while root.children:
        po(root.children[0], rlist)
        del root.children[0]
        rlist.append(root.val)
    return rlist
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        return po(root, [])