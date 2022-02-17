class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        new_s = list(s)
        new_t = list(t)
        for alpha in new_s:
            new_t.remove(alpha)
        return new_t[0]