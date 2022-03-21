class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        i = 0
        tmp = 0
        while i < len(nums):
            if nums[i] in mapper:
                return [mapper[nums[i]],i]
            tmp = target - nums[i]
            if tmp not in mapper:
                mapper[tmp] = i
            i += 1