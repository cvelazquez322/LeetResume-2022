# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def isEqual(root, reet):
    if root is None and reet is None:
        return True
        if root is None or reet is None:
        return False
    if root.val == reet.val:
                if isEqual(root.left, reet.right) and isEqual(root.right, reet.left):
           return True
                    return False
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return isEqual(root.left, root.right)