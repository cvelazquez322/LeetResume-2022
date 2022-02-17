class Solution:
    def maximum69Number (self, num: int) -> int:
        numlist =  [int(x) for x in str(num)]
        T = 1
        pos = 0
        while len(numlist) > pos:
            if numlist[pos] == 6:
                numlist[pos] = 9
                break
            pos += 1
        newnumlist = [str(x) for x in numlist]
        newnum = int("".join(newnumlist))
        return max(newnum, num)