class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        i = 0
        nums.sort()
        rlist = []
        while i < len(nums):
            if nums[i] == target:
                rlist.append(i)
            i += 1
        return rlist