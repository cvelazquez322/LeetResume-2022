# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def leafv(root, vlist):
    if not root.left and not root.right:
        vlist.append(root.val)
    if root.left:
        leafv(root.left, vlist)
    if root.right:
        leafv(root.right, vlist)
    return vlist
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = leafv(root1, [])
        l2 = leafv(root2, [])
        if len(l1) == len(l2):
            i = 0
            while len(l1) > i:
                if l1[i] != l2[i]:
                    return False
                i += 1
                    else:
            return False
        return True
        