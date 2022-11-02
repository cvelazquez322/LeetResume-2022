class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mapper = {}
        for x in nums:
            if x in mapper:
                mapper[x] += 1
            else:
                mapper[x] = 1
        rsum = 0
        for x in mapper:
            if mapper[x] == 1:
                rsum += x
                        return rsum