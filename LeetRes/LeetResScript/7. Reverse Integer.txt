class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        y = a[::-1]
        if x < 0: 
            y = y[:-1]
        l = int(y)
        if x < 0: 
            l = l * -1
        if l.bit_length() >= 32:
            return 0
        return l
        