# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def finder(root, rmap):
    if root.val not in rmap:
        rmap[root.val] = 1
    if root.left:
        finder(root.left, rmap)
    if root.right:
        finder(root.right, rmap)
    return rmap
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        lmap = finder(root, {})
        del lmap[min(lmap)]
        if lmap:
            return min(lmap)
        return -1
        