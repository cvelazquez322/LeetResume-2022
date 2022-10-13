# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def mbtHelper(nums):
    maxi = max(nums)
    pos = nums.index(maxi)
    newroot = TreeNode(maxi)
    nums.pop(pos)
    numl = nums[:pos]
    numr = nums[pos:]
    if numl:
        newroot.left = mbtHelper(numl)
    if numr:
        newroot.right = mbtHelper(numr) 
    return newroot
                class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        return mbtHelper(nums)
        