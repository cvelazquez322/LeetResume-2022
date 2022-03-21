class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if len(S) == 0:
            return ""
        alist= []
        nadic = {}
        slist = list(S)
        pos = 0
        rstr = ""
        for x in slist:
            if x.isalpha():
                alist.insert(0, x)
            else:
                nadic[pos] = x
            pos += 1
                for x in nadic:
            alist.insert(x, nadic[x])
        for x in alist:
            rstr += x
        return rstr