def helper(nums, currPoss, rlist):
    if len(nums) == 0:
        rlist.append(currPoss)
        return rlist
    for i in range(len(nums)):
        helper( nums[:i] + nums[i+1:], currPoss + [nums[i]], rlist)
    return rlist
                class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return helper(nums, [], [])