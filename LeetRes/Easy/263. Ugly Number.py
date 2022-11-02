class Solution:
    def isUgly(self, n: int) -> bool:
        while n >= 2:
            check = n
            if n >= 2 and n % 2 == 0:
                n = n//2
            if n >= 3 and n % 3 == 0:
                n = n//3
            if n >= 5 and n % 5 == 0:
                n = n//5
            if check == n:
                break
        return 1 == n