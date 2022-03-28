# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sumoftree(node, rlist):
    rlist[0] += node.val
    if node.left:
        sumoftree(node.left, rlist)
    if node.right:
        sumoftree(node.right, rlist)
    return rlist[0]
# value is whatever we get from sumoftree, rval stands for recursive value, which 
    is at position 0 within a list
# recursive value will build as we go through our function recursively
def convert(node, value, rval):
    if node.left:
        convert(node.left, value, rval)
    temp = node.val
    node.val = value - rval[0]
    rval[0] += temp
    if node.right:
        convert(node.right, value, rval)
    return node
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        startval = sumoftree(root, [0])
        return convert(root, startval, [0])