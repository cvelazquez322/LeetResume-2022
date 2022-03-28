class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxstr, pos = 0, 0
        for x in sentences:
            pos = len(x.split(' '))
            maxstr = max(maxstr, pos)
        return maxstr