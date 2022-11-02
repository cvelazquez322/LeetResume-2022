class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(' ')
        newS = ''
        for x in range(k):
            newS += s[x] + ' '
        newS = newS [:-1]
        return newS