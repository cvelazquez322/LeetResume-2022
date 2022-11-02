"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def maxD(root, cDep, mDep):
    mDep[0] = max(cDep,mDep[0])
    for i in range(len(root.children)):
        maxD(root.children[i], cDep + 1, mDep)
    return mDep[0]
        def lo(root, rlist, dep):
    rlist[dep].append(root.val)
    for i in range(len(root.children)):
        lo(root.children[i], rlist, dep+ 1)
        return rlist
            class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        mDep = maxD(root, 1, [1])
        rlist = []
        for i in range(mDep):
            rlist.append([])
        return lo(root, rlist, 0)
        