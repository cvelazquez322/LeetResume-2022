# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def solution(root, rlist):
    if root.left:
        solution(root.left, rlist)
    rlist.append(root.val)
    if root.right:
        solution(root.right, rlist)
    return rlist
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None
        pos = solution(root, [])
        try:
            for i in range(len(pos)):
                if pos[i] >= pos[i + 1]:
                    return False
        except:
            return True
        return True