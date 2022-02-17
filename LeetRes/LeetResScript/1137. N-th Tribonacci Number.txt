class Solution:
    def tribonacci(self, n: int) -> int:
        llist= [0, 1, 1]
        if n < 3:
            return llist[n]
        while n >= 3:
            new = llist[-1] + llist[-2] + llist[-3]
            llist.append(new)
            n -= 1
        return llist[-1]
            