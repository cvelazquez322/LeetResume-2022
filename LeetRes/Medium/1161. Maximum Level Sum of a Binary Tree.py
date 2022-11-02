# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root, dlist, cdep):
    if len(dlist) < cdep:
        dlist.append([0])
    dlist[cdep-1][0] += root.val
    if root.left:
        helper(root.left, dlist, cdep + 1)
    if root.right:
        helper(root.right, dlist, cdep + 1)
    return dlist
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        sList = helper(root, [], 1)
        cMax, lMax = sList[0][0], 1
        for i in range(len(sList)):
            if cMax < sList[i][0]:
                cMax = sList[i][0]
                lMax = i + 1
        #print(sList, lMax, cMax)
        return lMax
                            