class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numDict, trueDict = {}, {}
        for x in nums:
            if x * -1 in numDict:
                trueDict[abs(x)] = True
                        elif x not in numDict:
                numDict[x] = False
                        if trueDict:
            return max(trueDict)
        else:
            return -1