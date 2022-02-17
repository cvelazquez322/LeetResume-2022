class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        alist = {}
        for item in nums:
            if item not in alist:
                    alist[item] = True
            else:
                alist.pop(item)
        return alist