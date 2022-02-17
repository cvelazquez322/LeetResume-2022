class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        rlist = []
        for x in nums1:
            if x in nums2 and x not in rlist:
                rlist.append(x)
        return rlist
                