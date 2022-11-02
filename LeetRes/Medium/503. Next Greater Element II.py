class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        rlist, check = [], 0
        for i in range(len(nums)):
            newlist = nums[i + 1:] + nums[:i]
            for num in newlist:
                check = 0
                if num > nums[i]:
                    rlist.append(num)
                    check =1
                    break
            if check == 0:
                rlist.append(-1)
        return rlist
                