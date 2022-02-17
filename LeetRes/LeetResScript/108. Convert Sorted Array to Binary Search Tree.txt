import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        array_len = len(nums)
        if array_len == 0:
            return
        array_mid_index = int(math.ceil((array_len)/2) - 1)
        Head = TreeNode(nums[array_mid_index])
        if nums[:array_mid_index]:
            Head.left = self.sortedArrayToBST(nums[:array_mid_index])
        if nums[array_mid_index:]:
            Head.right = self.sortedArrayToBST(nums[array_mid_index + 1:])
                return Head