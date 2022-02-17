class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ln = len(nums)
        if ln == 0:
            return 0
        rn = 0
        i = 0
        if ln % 2 == 0:
            while ln > i:
                rn+= min(nums[i], nums[i+1])
                i += 2
        else:
            while ln > i:
                if i == ln - 1:
                    rn += nums[i]
                    i += 1
                    continue
                                    rn += min([nums[i], nums[i+1]])
                i += 2
        return rn