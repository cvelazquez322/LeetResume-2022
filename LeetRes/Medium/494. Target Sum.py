def rattempt(i, total, mapper, nums, target):
    if i == len(nums):
        return 1 if total == target else 0
    if (i, total) in mapper:
        return mapper[(i, total)]
    mapper[(i, total)] = (rattempt(i + 1, total + nums[i], mapper, nums, target) + 
                          rattempt(i + 1, total - nums[i], mapper, nums, target))
    return mapper[i, total]
    class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return rattempt(0, 0, {}, nums, target)