# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def pruner(root, target, parent):
    if root.val == target and not root.left and not root.right:
        if parent is None:
            root = None
            return
        if root is parent.right:
            root.val = 0
            parent.right = None
            return
        if root is parent.left:
            root.val = 0
            parent.left = None
            return
                if root.left:
        pruner(root.left, target, root)
    if root.right:
        pruner(root.right, target, root)
            if root is not None and root.val == target and not root.left and not root
        .right:
        print(root.val)
        pruner(root, target, parent)
           if root.val == target and not root.left and not root.right:    
        return None    
                return root
                if root.left:
        pruner(root.left, target, root)
    if root.right:
        pruner(root.right, target, root)
            if root.val == target and not root.left and not root.right:
        pruner(root, target, parent)
            return root
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None
        return pruner(root, target, None)