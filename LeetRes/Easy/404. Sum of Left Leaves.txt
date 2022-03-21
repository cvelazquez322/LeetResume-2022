# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lsHelper(root, rlist, T):
    if root.left:
        lsHelper(root.left, rlist, True)
        if root.right:
        lsHelper(root.right, rlist, False)
                if not root.left and not root.right:
        if T == True:
            rlist[0] += root.val
    return rlist[0]
    class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return lsHelper(root, [0], False)
        #s = 0
        #ilist = lsHelper(root, [], False)
                #for val in ilist:
        #    s+= val
        #return s
        