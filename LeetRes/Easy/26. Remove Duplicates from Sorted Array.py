class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lenth = len(nums)
        if lenth == 0:
            return 0
        pos = 0
        while lenth > pos + 1:
            if nums[pos] == nums[pos + 1]:
                nums.pop(pos + 1)
                lenth -= 1
                continue
            pos += 1
                        return lenth