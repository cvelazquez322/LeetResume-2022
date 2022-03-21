# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def minHelper(root, rlist, counter):
    counter += 1
    if not root.left and not root.right:
        rlist.append(counter)
    if root.left:
        minHelper(root.left, rlist, counter)
    if root.right:
        minHelper(root.right, rlist, counter)
    return rlist
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        rlist = minHelper(root, [], 0)
        rlist.sort()
        return rlist[0]
        