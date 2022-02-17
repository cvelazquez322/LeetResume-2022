class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        rlist = [''] * len(s)
        rstring = ''
        for i in range(len(s)):
            rlist[indices[i]] = s[i]
        for x in rlist:
            rstring += x
        return rstring