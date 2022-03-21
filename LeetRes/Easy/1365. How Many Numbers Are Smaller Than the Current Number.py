class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        rl = []
        for x in nums:
            i = 0
            counter = 0
            while len(nums) > i:
                if x > nums[i]:
                    counter += 1
                i += 1
            rl.append(counter)
                    return rl