class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        rlist = []
        olist = []
        if len(A) == 0:
            return 0
        for x in A:
            if x % 2 == 0:
                rlist.append(x)
            else:
                olist.append(x)
        return rlist + olist