# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def postHelper(root, ilist):
    if root.left:
        postHelper(root.left, ilist)
    if root.right:
        postHelper(root.right, ilist)
    ilist.append(root.val)
    return ilist
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        createdList = []
        return postHelper(root, createdList)