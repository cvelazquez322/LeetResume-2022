class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        if len(grid) == 0:
            return 0
        for alist in grid:
            for aint in alist:
                if aint < 0:
                    count += 1
        return count