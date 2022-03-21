# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def DepthHelper(root, x):
    x += 1
    if root.left and root.right:
       return max(DepthHelper(root.left, x), DepthHelper(root.right, x))
        if root.left:
        return DepthHelper(root.left, x)
    if root.right:
        return DepthHelper(root.right, x)
            if not root.left and not root.right:
        return x
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        num = 0
        if root is None:
            return num
        return DepthHelper(root, num)
        