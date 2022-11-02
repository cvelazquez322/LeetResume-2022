# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root, rlist):
    if root.left:
        helper(root.left, rlist)
    rlist.append(root)
    if root.right:
        helper(root.right, rlist)
    return rlist
def rightMaker(ilist):
    if len(ilist) > 1:
        ilist[0].left = None
        ilist[0].right = ilist[1]
        rightMaker(ilist[1:])
    if len(ilist) == 1:
        ilist[0].left = None
    return ilist[0]
                class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        return rightMaker(helper(root, []))
        