import random
class Solution:
    def sumZero(self, n: int) -> List[int]:
        rlist = []
        tempint = 0
        if n == 0:
            return 
        if n == 1:
            return [0]
        if n % 2 == 0:
            while len(rlist) != n:
                tempint = random.randint(1, n)
                if tempint in rlist:
                    continue
                else:
                    rlist.append(tempint)
                    rlist.append(tempint * -1)
        if n % 2 != 0:
            rlist.append(0)
            while len(rlist) != n:
                tempint = random.randint(1, n)
                if tempint in rlist:
                    continue
                else:
                    rlist.append(tempint)
                    rlist.append(tempint * -1)
        return rlist