# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def Alabama(root, depth, rval, parent, rlist):
    if root.val == rval:
        rlist.append([rval, depth, parent])
    if root.left:
        Alabama(root.left, depth + 1, rval, root, rlist)
    if root.right:
        Alabama(root.right, depth + 1, rval, root, rlist)
    return rlist
            class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False
        identityx = Alabama(root, 0, x, None, [])
        identityy = Alabama(root, 0, y, None, [])
        if identityx[0][1] == identityy[0][1]:
            if identityx[0][2] != identityy[0][2]:
                return True
        return False