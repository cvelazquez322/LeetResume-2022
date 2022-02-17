# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def gtcHelper(node, target, rlist):
    if node is None:
        return
    if node.val == target.val:
        rlist.append(node)
    if node.left:
        gtcHelper(node.left, target, rlist)
    if node.right:
        gtcHelper(node.right, target, rlist)
    return rlist
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
       # if original is None or cloned is None:
       #     return None
        return gtcHelper(cloned, target, [])[0]