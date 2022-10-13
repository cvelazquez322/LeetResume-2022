class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        if len(nums) >= 3:
            nums.sort()
            nums.reverse()
            return nums[2]
        else:
            return max(nums)