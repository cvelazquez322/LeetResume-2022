# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def preHelper(root, returned_list):
    if root is None:
        return None
    returned_list.append(root.val)
    if root.left:
        preHelper(root.left, returned_list)
            if root.right:
        preHelper(root.right, returned_list)
    return returned_list
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
           #ULR
        #value list
        vlist = []
        return preHelper(root, vlist)
                            