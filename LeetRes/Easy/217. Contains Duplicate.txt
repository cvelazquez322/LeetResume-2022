class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rmap = {}
        for x in nums:
            if x in rmap:
                return True
            else:
                rmap[x] = 1
        return False