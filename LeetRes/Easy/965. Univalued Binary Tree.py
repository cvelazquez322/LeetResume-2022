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
    #ULR
    #value list
    vlist = []
    return preHelper(root, vlist)
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        new_list = []
        new_int = 0
        new_list = preorderTraversal(root)
        if len(new_list) >= 1:
            new_int = new_list[0]
            for i in new_list:
                if new_int != i:
                    return False
            return True
                