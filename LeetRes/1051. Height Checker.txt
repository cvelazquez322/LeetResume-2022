class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        counter = 0
        a = sorted(heights)
        for i in range(0, len(heights)):
            if a[i] != heights[i]:
                counter += 1
        return counter
                        