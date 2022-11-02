def rhelper(r1,r2, nums):
    for n in range(len(nums)):
            temp = max(nums[n] + r1, r2)
            r1 = r2
            r2 = temp
    return r2
class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0,0
        if len(nums) > 1:
            return max(rhelper(r1,r2,nums[1:]), rhelper(r1,r2,nums[:-1]))
        return nums[0]