# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def iibstHelper(root, val, parent):
    if root is None:
        root = TreeNode(val)
        if root.val < parent.val:
            parent.left = root
        else:
            parent.right = root
                    if root.val > val:
        iibstHelper(root.left, val, root)
    if root.val < val:
        iibstHelper(root.right, val, root)
    return root
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        return iibstHelper(root, val, None)
        