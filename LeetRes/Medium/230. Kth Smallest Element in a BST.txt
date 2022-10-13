# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root, rlist):
    if root.left:
        inorder(root.left, rlist)
    rlist.append(root.val)
    if root.right:
        inorder(root.right, rlist)
    return rlist
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        rootlist = inorder(root, [])
        return rootlist[k -1]