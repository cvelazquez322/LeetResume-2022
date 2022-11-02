import math
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
                for i in range(math.floor(len(s)/2)):
            s[i], s[-1*(i+ 1)] = s[-1*(i+ 1)], s[i]