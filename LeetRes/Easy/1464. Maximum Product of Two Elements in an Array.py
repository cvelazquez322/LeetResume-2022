class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = max(nums[0], nums[1]), min(nums[0], nums[1])
        for item in nums[2:]:
            if item > first:
                second = first
                first = item
                            elif item > second:
                second = item
        return (first-1) * (second-1)
                            