class Solution:
    def getSum(self, a: int, b: int) -> int:
                mask = 0xffffffff
                while b & mask:
            carry = a & b
            a = a ^ b
            b = carry << 1
                # for overflow condition like
        # -1
        #  1
        return (a & mask) if b > mask else a