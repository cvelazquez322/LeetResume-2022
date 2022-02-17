class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum = 0
        for x in accounts:
            cursum = sum(x)
            if cursum > maxsum:
                maxsum = cursum
        return maxsum