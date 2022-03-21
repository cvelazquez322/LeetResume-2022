class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nlist = []
        i = 0
        while i < len(nums):
            nlist.append(nums[nums[i]])
            i += 1
        return nlist