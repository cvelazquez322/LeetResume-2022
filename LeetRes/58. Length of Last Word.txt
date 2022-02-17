class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        if len(a) == 0:
            return 0
        z = a[-1]
        x =  len(z)
        return x
        