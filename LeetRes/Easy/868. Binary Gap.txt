def gapcheck(nums):
    pos = 0
    rlist = []
    while len(nums) > pos + 1:
        rlist.append(nums[pos + 1] - nums[pos])
        pos += 1
    return max(rlist)
        class Solution:
    def binaryGap(self, N: int) -> int:
        if N == 0:
            return 0
        ilist = list(bin(N)[2:])
        poslist = []
        pos = 0
        while len(ilist) > pos:
            if ilist[pos] == '1':
                poslist.append(pos)
            pos += 1
        print(poslist)
        if len(poslist) < 2:
            return 0
        else:
            return gapcheck(poslist)
                        