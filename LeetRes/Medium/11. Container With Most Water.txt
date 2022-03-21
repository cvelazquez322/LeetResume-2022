class Solution:
    def maxArea(self, height: List[int]) -> int:
        possmax = 0
        currmax = 0
        i = 0
        j = len(height) -1 
                while i < j:
                smaller = min(height[j], height[i])
                possmax = (j - i) * smaller
                if possmax > currmax:
                    currmax = possmax
                                if height[i] < height[j]:
                    i += 1
                else:
                    j -= 1
                                                return currmax