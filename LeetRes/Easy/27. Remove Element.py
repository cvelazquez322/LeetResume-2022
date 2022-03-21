class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        pos = 0
        counter = 0
        while len(nums) > pos:
            if nums[pos] == val:
                nums.pop(pos)
                counter += 1
                pos -= 1
            pos += 1
        return len(nums)