class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        alist = []
        for item in nums:
            if item not in alist:
                    alist.append(item)
            else:
                alist.remove(item)
        return alist[0]
        