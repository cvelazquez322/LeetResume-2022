class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rlist = []
        for num in nums1:
            i = nums2.index(num)
            if nums2[i:]:
                check = 0
                for item in nums2[i:]:
                    if item > nums2[i]:
                        rlist.append(item)
                        check = 1
                        break
                if check == 0:
                    rlist.append(-1)
        return rlist
                        