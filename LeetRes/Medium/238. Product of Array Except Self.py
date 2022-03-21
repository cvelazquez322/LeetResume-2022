class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rlist = [1] * len(nums)
        post, pre = 1, 1
        for i in range(len(nums)):
            rlist[i] = pre
            pre *= nums[i]
                for i in range(len(nums) -1, -1, -1):
            rlist[i] *= post
            post *= nums[i]
            i -= 1
        return rlist