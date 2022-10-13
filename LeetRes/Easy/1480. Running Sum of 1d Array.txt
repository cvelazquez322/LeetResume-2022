class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newlist = []
        lsum = 0
        for x in nums:
            lsum += x
            newlist.append(lsum)
        return newlist