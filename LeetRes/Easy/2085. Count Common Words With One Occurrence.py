class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        mapper1, mapper2 = {}, {}
        for x in words1:
            if x in mapper1:
                mapper1[x] += 1
            else:
                mapper1[x] = 1
        for x in words2:
            if x in mapper2:
                mapper2[x] += 1
            else:
                mapper2[x] = 1
        counter = 0
        for x in mapper1:
            if mapper1[x] == 1 and x in mapper2:
                if mapper2[x] == 1:
                    counter += 1
        return counter