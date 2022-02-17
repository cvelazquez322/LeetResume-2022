# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def rlthelper(root, istring, rlist):
    istring += str(root.val)
    if root.left:
        rlthelper(root.left, istring, rlist)
        if root.right:
        rlthelper(root.right, istring, rlist)
            if not root.left and not root.right:
        rlist.append(int(istring, 2))
    return rlist
                class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        rnum = rlthelper(root, '', [])
        sumofroot = 0
        for rootval in rnum:
            sumofroot += rootval
        return sumofroot