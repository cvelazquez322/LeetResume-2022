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
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #LUR
        #value list
        vlist = []
        return inHelper(root, vlist)    