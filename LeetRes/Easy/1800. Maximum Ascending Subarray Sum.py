class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currMax, possMax, prev = 0,0, 0
        for i in range(len(nums)):
            if nums[i] <= prev:
                possMax = 0
                            prev = nums[i]
            possMax += nums[i]
                        currMax = max(currMax, possMax)
        return currMax