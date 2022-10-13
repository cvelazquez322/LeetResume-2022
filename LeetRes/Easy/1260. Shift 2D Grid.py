class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        while k > 0:
            remainder = [0,0]
            for row in grid:
                if remainder[0]:
                    row.insert(0, remainder[-1])
                row[:], remainder = row[:-1], [1, row[-1]]
            # give the remainder of the last row back to the first row
            grid[0].insert(0, remainder[-1])
            k -= 1
        return grid