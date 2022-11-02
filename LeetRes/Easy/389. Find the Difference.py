class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapper = {}
        for i in s:
            if i in mapper:
                mapper[i] += 1
            else:
                mapper[i] = 1
        for i in t:
            if i in mapper:
                mapper[i] -= 1
                if mapper[i] == 0:
                    del mapper[i]
            else:
                return i
            