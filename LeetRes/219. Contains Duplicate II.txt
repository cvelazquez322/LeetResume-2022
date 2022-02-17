class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
                pos = 0
        while len(nums) > pos:
            pos2 = pos + 1
            while len(nums) > pos2:
                if nums[pos] == nums[pos2]:
                    if abs(pos2 - pos) <= k:
                        return True
                pos2 += 1 
            pos += 1
        return False