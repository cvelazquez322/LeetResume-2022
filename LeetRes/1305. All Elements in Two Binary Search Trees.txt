# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inordert(root, rlist):
    if root.left:
        inordert(root.left, rlist)
    rlist.append(root.val)
    if root.right:
        inordert(root.right, rlist)
    return rlist
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if root1 and not root2:
            return inordert(root1, [])
        if root2 and not root1:
            return inordert(root2, [])
                list1 = inordert(root1, [])
        list2 = inordert(root2, [])
        rlist = []
        while list1 or list2:
            if list1 and list2:
                if list1[0] <= list2[0]:
                    rlist.append(list1[0])
                    list1.pop(0)
                    continue
                else:
                    rlist.append(list2[0])
                    list2.pop(0)
                    continue
            if list1:
                rlist += list1
                list1 = []
                continue
                            if list2:
                rlist += list2
                list2 = []
                continue
        return rlist
                    