class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        pos  =  0
        while True:
            if nums[pos] == target:
                return pos
            if nums[pos] > target:
                return pos 
            if len(nums) - 1 == pos:
                return pos + 1
            pos += 1