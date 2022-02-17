class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        i = 0
        sumo = 0
        curr_summ = sum(nums)
        while(len(nums) > 0):
            if sumo == curr_summ - nums[0]:
                return i
                        curr_summ -= nums[0]
            sumo += nums.pop(0)
            i+= 1
        return -1
                                        