# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traversal(root, path, plist, depth):
    if depth != 0:
        path += "->" + str(root.val)
    else:
        path += str(root.val)
    depth += 1
    if root.left is None and root.right is None:
        plist.append(path)
    if root.left:
        traversal(root.left, path, plist, depth)
    if root.right:
        traversal(root.right, path, plist, depth)
    return plist
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return ""
        return traversal(root, "", [], 0)