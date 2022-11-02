def maximumSubarrayHelper(ilist):
    i, currmax, currposs = 1, ilist[0], ilist[0]
    while i < len(ilist):
        currposs += ilist[i]
                if currposs < ilist[i]:
            currposs = ilist[i]
                if currposs > currmax:
            currmax = currposs
                i += 1
    return currmax
    class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        return maximumSubarrayHelper(nums)