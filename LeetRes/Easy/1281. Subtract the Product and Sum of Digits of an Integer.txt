class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nl = list(str(n))
        sumo = 0
        prod = 1
        for x in nl:
            sumo += int(x)
            prod *= int(x)
        return prod - sumo