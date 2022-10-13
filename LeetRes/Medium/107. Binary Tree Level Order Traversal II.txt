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
def sol(root, plist, depth):
    plist[depth].append(root.val)
    if root.left:
        sol(root.left, plist, depth + 1)
    if root.right:
        sol(root.right, plist, depth + 1)
    return plist[::-1]
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        return sol(root, ListMaker(TreeHeight(root, 0)), 0)