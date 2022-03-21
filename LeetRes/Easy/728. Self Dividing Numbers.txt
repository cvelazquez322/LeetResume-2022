def selfdiv(aint):
    aintlist = list(str(aint))
    for x in aintlist:
        if int(x) == 0:
            return False
        if aint % int(x) != 0:
            return False
    return True
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        if left == 0 and right == 0:
            return 0
        mini = min(left, right)
        maxi = max(left, right)
        rlist = []
                i = mini
                while maxi >= i:
            if selfdiv(i):
                rlist.append(i)
            i+= 1
        return rlist
                