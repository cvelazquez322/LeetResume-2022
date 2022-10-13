def nosHelper(num, step):
    if num == 0:
        return step
    step += 1
    if num % 2 == 0:
        num /= 2
        return nosHelper(num, step)
    else:
        num -= 1
        return nosHelper(num, step)
        class Solution:
    def numberOfSteps (self, num: int) -> int:
        return nosHelper(num, 0)
        