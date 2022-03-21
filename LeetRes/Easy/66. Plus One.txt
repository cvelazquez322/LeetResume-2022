class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = -1
        length = (-1 * len(digits))
        while(i != 0):
            if digits[i] == 10:
                digits[i] = 0
                if i > length:
                    digits[i-1] += 1
                else:
                    digits.insert(i, 1)
                i -= 1
            else:
                i = 0
                        return digits
        