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
def postorderTraversal(root):
    if root is None:
        return 0
    createdList = []
    return postHelper(root, createdList)
class Solution:
        def findTilt(self, root: TreeNode) -> int:
            def t(r):
                if not r: return 0
                a, b = t(r.left), t(r.right)
                self.s += abs(a - b)
                return a + b + r.val
            self.s = 0
            t(root)
            return self.s