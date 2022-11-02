class Solution:
    def sortSentence(self, s: str) -> str:
        llist = s.split(' ')
        mapper = {}
        for x in llist:
            mapper[int(x[-1])] = x[:-1]
        newS = ''
        for x in range(1, len(llist) + 1):
            newS += mapper[x] + ' '
        newS = newS[:-1]
        return newS