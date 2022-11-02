class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        two = 4
        while two <= n:
            n = n/two
        return 1 == n