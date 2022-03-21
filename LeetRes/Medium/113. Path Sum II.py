# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sol(root, value, valStr, target, rlist):
    value += root.val
    valStr += str(root.val) + " "
    if root.left is None and root.right is None and value == target:
        rlist.append(valStr.split())
    if root.left:
        sol(root.left, value, valStr, target, rlist)
    if root.right:
        sol(root.right, value, valStr, target, rlist)
    return rlist
        class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> 
        List[List[int]]:
        if root is None:
            return []