class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while 2 <= n:
            n = n/2
        return 1 == n