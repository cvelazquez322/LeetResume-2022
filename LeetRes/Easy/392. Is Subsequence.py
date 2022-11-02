def sHelper(sub, full):
    if len(full) == 0 or len(sub) == 0:
        return len(sub) == 0
        if sub[0] == full[0]:
        sub = sub[1:]
        return sHelper(sub, full[1:])
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return sHelper(s, t)