# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def solution(root, val):
    if root.val == val:
        return root
    if val > root.val and root.right:
        return solution(root.right, val)
    if val < root.val  and root.left:
        return solution(root.left, val)
    return None
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        return solution(root, val)