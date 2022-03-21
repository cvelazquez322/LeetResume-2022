class Solution:
    def isHappy(self, n: int) -> bool:
        at = {}
        while(True):
            n = list(str(n))
            i = 0
                        while len(n) > i:
                                n[i] = (int(n[i])) * (int(n[i]))
                                i += 1
            i= 0
            counter  = 0
            while len(n) > i:
                                counter += n[i]
                i += 1
            if counter == 1:
                return True
            if counter in at:
                return False
            if counter not in at:
                at[counter] = False
            n = counter
                    