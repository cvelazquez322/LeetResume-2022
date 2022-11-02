class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r)// 2
            if mid*mid == x :
                return mid
            elif (mid - 1) *(mid-1) < x and  (mid) * (mid) > x:
                return mid - 1
                        elif mid * mid > x:
                r = mid - 1
                        else:
                l = mid + 1
        return 0