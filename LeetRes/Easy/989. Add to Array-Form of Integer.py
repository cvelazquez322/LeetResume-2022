class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i, klist = 0, [int(item) for item in str(k)]
        while len(num) != len(klist):
            if len(num) > len(klist):
                klist.insert(0,0)
            else:
                num.insert(0,0)
                        for i in range(len(klist)):
            num[-i-1] += klist[-i - 1]
            if num[-i-1] >= 10:
                num[-i-1] -= 10
                if num[:-i-1]:
                    num[-i-2] += 1
                else:
                    num.insert(0,1)
        return num
                                