# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def bstHelper(node1, node2):
    if node1.val > node2.val:
        if node1.left:
            bstHelper(node1.left, node2)
        if not node1.left:
            node1.left = node2
    if node1.val < node2.val:
        if node1.right:
            bstHelper(node1.right, node2)
        if not node1.right:
            node1.right = node2
    return node1
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        i = 1
        root = TreeNode(preorder[0])
        while i < len(preorder):
            newnode = TreeNode(preorder[i])
            bstHelper(root, newnode)
            i += 1
        return root