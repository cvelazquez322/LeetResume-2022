class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        bot, tmp, top = 0, 0, 1
        while n -1:
            tmp = top
            top = bot + top
            bot = tmp
            n -= 1
        return top