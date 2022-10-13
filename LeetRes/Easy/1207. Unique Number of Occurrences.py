class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapper = {}
        for x in arr:
            if x in mapper:
                mapper[x] += 1
            else:
                mapper[x] = 1
                invMapper = {}
        for x in mapper:
            if mapper[x] in invMapper:
                return False
            else:
                invMapper[mapper[x]] = x
        return True