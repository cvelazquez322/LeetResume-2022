# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def preHelper(root, returned_list):
    returned_list.append(root.val)
    if root.left:
        preHelper(root.left, returned_list)
            if root.right:
        preHelper(root.right, returned_list)
    return returned_list
    def preorderTraversal(root):
    if root is None:
        return
    #ULR
    #value list
    vlist = []
    return preHelper(root, vlist)
def check0s(root):
    tmplist = []
    tmplist = preorderTraversal(root)
    for i in tmplist:
        if i != 0:
            return False
    return True
def pruneHelper(root):
    if root.left:
        if check0s(root.left):
            root.left = None
    if root.right:
        if check0s(root.right):
            root.right = None
    if root.left:
        pruneHelper(root.left)
    if root.right:
        pruneHelper(root.right)
    return root    
                            class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        return pruneHelper(root)
                   