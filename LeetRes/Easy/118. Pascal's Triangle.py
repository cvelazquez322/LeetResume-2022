def pasc(nr, rlist):
    if nr == 0:
        return rlist
    ilist = rlist[-1].copy()
    ilist = [0] + ilist + [0]
    try:
        for i in range(len(ilist)):
                ilist[i] = ilist[i] + ilist[i+1]
    except:
        rlist.append(ilist[:-1])
            return pasc(nr-1, rlist)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
                return pasc(numRows - 1, [[1]])