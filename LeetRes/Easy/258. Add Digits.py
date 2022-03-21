def spliter(intx):
    listx = [int(x) for x in str(intx)]
    summed = sum(listx)
    if len(str(summed)) > 1:
        return spliter(summed)
    else:
        return summed
    class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return spliter(num)