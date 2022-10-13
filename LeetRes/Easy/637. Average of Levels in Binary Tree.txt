# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# problem asks that i solve to make a list of the averages at each level.
# idea, make a list of lists.
# the list will hold a list, each sublist will have 2 values,
# one being the sum, the other being the num of nodes at this level:
def TreeHeight(root, hcounter):
    if root is None:
        return 0
    hcounter += 1
    if root.left:
        return max(TreeHeight(root.left, hcounter), TreeHeight(root.right, 
            hcounter))
    if root.right:
        return max(TreeHeight(root.left, hcounter),TreeHeight(root.right, hcounter
            ))
    if root.right is None and root.left is None:
        return hcounter
#returns a list of lists, always with a prebuilt value of [0,0], as long as the 
    num it is given
def ListMaker(num):
    parentList = []
    while num != 0:
        parentList.append([0,0])
        num -= 1
    return parentList
#expects root, a list of lists with each one containing [0,0], and current depth 
    of the tree initialized at 0
#returns a list of nodes, the values at plist[depth][0] and the amount of nodes at 
    plist[depth][1] 
def nodeVal(root, plist, depth):
    plist[depth][0] += root.val
    plist[depth][1] += 1
    if root.left:
        nodeVal(root.left, plist, depth + 1)
    if root.right:
        nodeVal(root.right, plist, depth + 1)
    return plist
#expects a list of lists, each one containing the list of values and the amount of 
    nodes on that level
#divides first number by second, adds to a list and then returns that value
def sol(plist):
    rlist = []
    for nodelist in plist:
        if nodelist [0] == 0:
            rlist.append(0)
            continue
        rootaver= round(nodelist[0]/nodelist[1], 5)
        rlist.append(rootaver)
    return rlist
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        return sol(nodeVal(root, ListMaker(TreeHeight(root, 0)), 0))
        