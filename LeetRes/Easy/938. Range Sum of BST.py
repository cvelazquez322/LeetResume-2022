# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def preorder(root, rlist):
        rlist.append(root.val)
        if root.left:
        preorder(root.left, rlist)
    if root.right:
        preorder(root.right, rlist)
    return rlist
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return None
        mini = min(L, R)
        maxi = max(L, R)
        sumo = 0
        rlist = preorder(root, [])
                for x in rlist:
            if mini <= x and maxi >= x:
                sumo += x
        return sumo