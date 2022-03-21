# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def sbstHelper(root, val, rlist):
    if root.val == val:
        rlist[0] = root
    if root.left:
        sbstHelper(root.left, val, rlist)
    if root.right:
        sbstHelper(root.right, val, rlist)
    return rlist[0]
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        return sbstHelper(root, val, [None])
        