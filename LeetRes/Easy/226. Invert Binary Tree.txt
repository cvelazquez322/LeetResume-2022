# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def itreeHelper(root, newtree):
        if root is None:
        return None
        newtree = TreeNode(root.val)
        if root.left:
        newtree.right = itreeHelper(root.left, newtree)
            if root.right:
        newtree.left = itreeHelper(root.right, newtree)
        return newtree
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        newtree = TreeNode(0)
        return itreeHelper(root, newtree)
        