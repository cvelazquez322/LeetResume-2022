# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def prune(node):
            if not node:
                return None
            if node.val > high:
                return prune(node.left)
            if node.val < low:
                return prune(node.right)
            node.left = prune(node.left)
            node.right = prune(node.right)
            return node
        return prune(root)