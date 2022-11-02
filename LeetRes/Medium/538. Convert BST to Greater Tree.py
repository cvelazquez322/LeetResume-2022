# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def inHelper(root, returned_list):
    if root is None:
        return None
    if root.left:
        inHelper(root.left, returned_list)
    returned_list.append(root.val)
            if root.right:
        inHelper(root.right, returned_list)
    return returned_list
    def inorderTraversal(root):
    #ULR
    #value list
    vlist = []
    return inHelper(root, vlist)
def convertBSTHelper(root, valist):
    summed = 0
    for x in valist:
        if root.val < x:
            summed += x
    root.val += summed
    if root.left:
        convertBSTHelper(root.left, valist)
    if root.right:
        convertBSTHelper(root.right, valist)
    return root
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        vlist = inorderTraversal(root)
        return convertBSTHelper(root, vlist)