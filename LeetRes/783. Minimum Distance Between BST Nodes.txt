# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(root, rlist):
    if root.left:
        helper(root.left, rlist)
    rlist.append(root.val)
    if root.right:
        helper(root.right, rlist)
    return rlist
                                            class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            inorder = helper(root, [])
            minimum = 0
            for i in range(len(inorder)):
                try:
                    if not minimum:
                        minimum = abs(inorder[i] - inorder[i + 1])
                    tmp = abs(inorder[i] - inorder[i + 1])
                    if tmp < minimum:
                        minimum = tmp
                                except:
                    return minimum 
        return minimum
        