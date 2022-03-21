# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def BLHelper(root, returned_list, depth, lcount):
    depth +=1
    returned_list.append([depth, lcount, root.val])
        if root.left:
        lcount += 1
        BLHelper(root.left, returned_list, depth, lcount)
            if root.right:
        lcount -= 1
        BLHelper(root.right, returned_list, depth, lcount)
    return returned_list
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
            #value list
        vlist = []
        #returns list of nodes: depth, "Left value", and val of node
        #Left value == how many left nodes it took to get there.
        #Left value was decrimented by one for every right it took
        tmp = BLHelper(root, vlist, 0, 0)
        tmp.sort()
        return tmp[-1][2]        