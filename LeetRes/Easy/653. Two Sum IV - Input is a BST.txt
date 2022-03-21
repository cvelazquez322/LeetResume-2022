# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorderTraversal(root, valist):
    valist.append(root.val)
    if root.left:
        preorderTraversal(root.left, valist)
    if root.right:
        preorderTraversal(root.right, valist)
    return valist
def solution1(valist, tar):
    i = 0
    size = len(valist)
    while i <= size - 1 :
        j = i + 1
        while j <= size - 1:
            if valist[i] + valist[j] == tar:
                return True
            j += 1
        i += 1
    return False
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return None
                return solution1(preorderTraversal(root, []), k)
        