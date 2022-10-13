class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1, words2 = s1.split(' '), s2.split(' ')
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
        rlist = []
        for x in mapper1:
            if mapper1[x] == 1 and x not in mapper2:
                rlist.append(x)
                        for x in mapper2:
            if mapper2[x] == 1 and x not in mapper1:
                rlist.append(x)
        return rlist