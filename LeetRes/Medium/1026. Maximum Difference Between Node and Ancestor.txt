# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def solutionHelper(root, slist, currval):
    tmplist = slist.split(' ')
    if tmplist[-1] == '':
        tmplist.pop(-1)
    for x in tmplist:
        #print(tmplist, x)
        if abs(int(x) - root.val) > currval:
            currval = abs(int(x) - root.val)
        if len(tmplist) >= 2:
        slist = str(min(int(tmplist[0]), root.val, int(tmplist[1]))) + ' ' + str
            (max(int(tmplist[0]), root.val, int(tmplist[1])))
    else:
        slist += str(root.val) + ' '
        if root.left and root.right:
        return max(solutionHelper(root.left, slist, currval), solutionHelper(root
            .right, slist, currval))
    if root.left:
        return solutionHelper(root.left, slist, currval)
    if root.right:
        return solutionHelper(root.right, slist, currval)
        if root.left and root.right:
        return max(solutionHelper(root.left, slist, currval), solutionHelper(root
            .right, slist, currval))
    if root.left:
        return solutionHelper(root.left, slist, currval)
    if root.right:
        return solutionHelper(root.right, slist, currval)
    return currval
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        else:
            return solutionHelper(root, '', 0)