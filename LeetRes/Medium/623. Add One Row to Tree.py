# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sHelper(root, val, depth, lr, parent):
    if depth == 0:
        if lr:
            newNode = TreeNode(val)
            newNode.left = root
            parent.left = newNode
        else:
            newNode = TreeNode(val)
            newNode.right = root
            parent.right = newNode
        return
    if root and depth:
        sHelper(root.left, val, depth-1, 1, root)
    if root and depth:
        sHelper(root.right, val, depth-1, 0, root)
    return root
        class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode
        return sHelper(root, val, depth -1, 0, None)