# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def inoT(root, rlist):
    if root.left:
        inoT(root.left, rlist)
    rlist.append(root.val)
    if root.right:
        inoT(root.right, rlist)
    return rlist
def ibstHelper(nums):
    if nums:
        newroot = TreeNode(nums.pop(0))
    if nums:
        newroot.right = ibstHelper(nums)
    return newroot
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
            if root is None:
                return None
            ilist = inoT(root, [])
            return ibstHelper(ilist)