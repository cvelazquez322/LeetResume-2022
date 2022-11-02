# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sHelper(r1, r2):
    if r1 and r2:
        r1.val = r1.val + r2.val
    if r1.left and r2.left:
        sHelper(r1.left,r2.left)
    if r2.left and r1.left == None:
        r1.left = r2.left
    if r1.right and r2.right:
        sHelper(r1.right,r2.right)
    if r2.right and r1.right == None:
        r1.right = r2.right
    return r1
        class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1== None:
            return root2
        if root2 == None:
            return root1
        return sHelper(root1,root2)