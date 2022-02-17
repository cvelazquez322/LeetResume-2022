class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        lenth = len(nums)
        if lenth in [0, 1, 2]:
            return True
                i = 0
        while lenth > i:
            var = nums[i]
            nums.pop(i)
            pos = 0
            while lenth - 1 > pos + 1:
                if nums[pos] > nums[pos + 1]:
                    break
                if pos + 2 == lenth - 1:
                    return True
                pos += 1
            nums.insert(i, var)
            i += 1
                    return False