class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
                slist = list(s)
        tlist = list(t)
        tlen = len(tlist)
        while tlen != 0:
            if tlist[0] in slist:
                slist.remove(tlist[0])
                tlist.pop(0)
                tlen -= 1
            else:
                return False
        if len(slist) > 0:
            return False
        return True