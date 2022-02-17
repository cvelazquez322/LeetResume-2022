class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curr = 0
        maxcurr = 0
        for x in nums:
            if x == 1:
                curr += 1
            else:
                curr = 0
            if curr >= maxcurr:
                maxcurr = curr
        return maxcurr
                    