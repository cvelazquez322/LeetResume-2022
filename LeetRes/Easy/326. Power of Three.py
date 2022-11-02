class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        two = 3
        while two <= n:
            n = n/two
        return 1 == n