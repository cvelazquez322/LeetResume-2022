class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = 0
        firsti = 0
        second  = 0
        i = 0
        for x in nums:
            if x > first:
                if first > second:
                    second = first
                first = x
                firsti = i
            if x < first and x > second:
                second = x
            i += 1
        if first >= second * 2:
            return firsti
        else:
            return -1
                