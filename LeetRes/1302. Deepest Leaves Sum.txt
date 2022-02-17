# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def dlsHelper(root, rlist, dep):
    if root is None:
        return
    dep += 1
    rlist.append([dep, root.val])
    if root.left:
        dlsHelper(root.left, rlist, dep)
    if root.right:
        dlsHelper(root.right, rlist, dep)
    return rlist
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return None
        rlist = dlsHelper(root, [], 0)
        print(rlist)
        rlist.sort()
        rlist.reverse()
        i = 0
        rn = 0
        print(rlist)
        maxd = rlist[0][0]
        while rlist[i][0] == maxd:
            rn += rlist[i][1]
            i += 1
        return rn
                    