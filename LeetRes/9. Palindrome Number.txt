import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        numlist = list(str(x))
        length = len(numlist)
        i = 0
        if length % 2 == 0:
            while i < length/2:
                if numlist[i] != numlist[-(i + 1)]:
                    return False
                i += 1
        else:
            while i + 1 < math.ceil(length/2):
                if numlist[i] != numlist[-(i + 1)]:
                    return False
                i += 1
                    return True
            