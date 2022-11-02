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
    def getRow(self, rowIndex: int) -> List[int]:
        return pasc(rowIndex, [[1]])[-1]