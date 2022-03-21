class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        rnum = 1
        temp = 0
        rdict = {}
        if num > 1:
            for x in range(2, num):
                if x in rdict:
                    break
                if num % x == 0:
                    temp = num / x
                    rnum += x + temp
                    rdict[temp] = True
                #print(rnum)
                else:
                    temp = num // x
                    rdict[temp] = True
                #print(rnum)
            if rnum == num:
                return True
                        else:
                return False
                    else:
            return False
        