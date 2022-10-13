class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mapper = {}
        for x in arr:
            if x in mapper:
                mapper[x] += 1
            else:
                mapper[x] = 1
        for x in mapper:
            if mapper[x] > len(arr) * (0.25):
                return x