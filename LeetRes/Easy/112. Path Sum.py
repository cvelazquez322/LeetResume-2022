# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def pathSumHelper(root, currVal, tarVal):
    if root is None:
        return False
    currVal += root.val
    if currVal == tarVal and root.left is root.right is None:
        return True
            return pathSumHelper(root.left, currVal, tarVal) or pathSumHelper(root.right, 
        currVal, tarVal)
            class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return pathSumHelper(root, 0, targetSum)