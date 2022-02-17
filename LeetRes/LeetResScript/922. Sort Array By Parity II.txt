class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        elist = []
        olist = []
        rlist = []
        if len(A) == 0:
            return 0
        for x in A:
            if x % 2 == 0:
                elist.append(x)
            else:
                olist.append(x)
        i = 0
        while len(elist) != 0 or len(olist) != 0:
                if i % 2 == 0:
                    rlist.append(elist.pop(0))
                else:
                    rlist.append(olist.pop(0))
                i += 1
                        return rlist