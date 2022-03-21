# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
                lower, upper = 1, n
                while lower <= upper:
                        mid = lower + (upper - lower)//2
                        query = guess(mid)
            if query == 0:
                # Hit:
                # guess number is the same as hidden number
                return mid
                        elif query == 1:
                # hidden number is larger than guessing
                lower = mid+1
                            else:
                # hidden number is smaller than guessing
                upper = mid-1
                        