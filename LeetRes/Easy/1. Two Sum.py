class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper, i = {}, 0
        for num in nums:
            if target - num in mapper:
                return [mapper[target-num], i]
            else:
                mapper[num] = i
            i += 1
            