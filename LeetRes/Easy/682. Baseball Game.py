class Solution:
    def calPoints(self, ops: List[str]) -> int:
        newList = []
        for x in ops:
            if x == 'C':
                newList = newList[:-1]
            elif x == 'D':
                newList.append(newList[-1] * 2)
            elif x == '+':
                newList.append(newList[-1] + newList[-2])
            else:
                newList.append(int(x))
        return sum(newList)