# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
p_list = []
def returnedlist(p):
    if p == None:
        return []
    p_list.append(p.val)
    if not p.left and p.right:
        p_list.append(None)
    if p.left:
        returnedlist(p.left)
    if p.right:
        returnedlist(p.right)
    return p_list
class Solution:    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        list1 = []
        list2 = []
        list1 = returnedlist(p).copy()
        p_list.clear()
        list2 = returnedlist(q).copy()
        p_list.clear()
        if list1 == list2:
            return True
        else:
            return False