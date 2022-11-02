# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def solution(root, rbool, prev):
    if root.left:
        solution(root.left,rbool, prev)
            if prev[0] == None:
        prev[0] = root.val
    else:
        if prev[0] >= root.val:
            rbool[0] = False
        prev[0] = root.val
                    if root.right:
        solution(root.right,rbool, prev)
        return rbool[0]
            class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None
        return solution(root, [True], [None])