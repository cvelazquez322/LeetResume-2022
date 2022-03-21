# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# expects a node and a number originally set at 0
# returns the height of said tree node, if node is none, returns 0
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
def ListMaker(num):
    parentList = []
    while num != 0:
        parentList.append([])
        num -= 1
    return parentList
#expects Node, list of lists starting as empty, and the current depth
#returns List of node values in a list of lists, in level order traversal
def LevelOrderHelper(root, rlists, depth):
    rlists[depth].append(root.val)
    depth += 1
    if root.left:
        LevelOrderHelper(root.left, rlists, depth)
    if root.right:
        LevelOrderHelper(root.right, rlists, depth)
    return rlists
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        return LevelOrderHelper(root, ListMaker(TreeHeight(root, 0)), 0)