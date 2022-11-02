# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def eHelper(root):
    if not root.left and not root.right:
        return root.val
    if root.val == 2:
        return eHelper(root.left) or eHelper(root.right)
    if root.val == 3:
        return eHelper(root.left) and eHelper(root.right)
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return eHelper(root)