class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        currSum, prev = sum(nums), 0
        for i in range(len(nums)):
            currSum -= nums[i]
            if prev == currSum:
                return i
            prev += nums[i]
        return -1
        