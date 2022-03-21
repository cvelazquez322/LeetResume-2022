class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        if len(nums) == 0 or len(index) == 0:
            return []
        rlist = []
        for x in range(0, len(nums)):
            rlist.insert(index[x], nums[x])
        return rlist