class Solution:
    def climbStairs(self, n: int) -> int:
        prev, nex = 0, 1
        for i in range(n):
            nex, prev = nex + prev, nex
        return nex