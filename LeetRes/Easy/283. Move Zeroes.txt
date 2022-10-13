class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lennums = len(nums)
        zlist = []
        if lennums == 0:
            return []
        pos = 0
        while len(nums) > pos:
            if nums[pos] == 0:
                zlist.append(0)
                nums.remove(0)
                pos -= 1
            pos += 1
        nums += zlist
        return 