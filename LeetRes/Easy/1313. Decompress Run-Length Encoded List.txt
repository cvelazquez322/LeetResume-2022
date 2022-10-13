class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) % 2 != 0:
            return []
        tmp = 0
        rlist = []
        while len(nums) != 0:
            tmplist = []
            tmp = nums[0]
            for x in range(0, tmp):
                tmplist.append(nums[1])
            nums.pop(0)
            nums.pop(0)
            rlist += tmplist
        return rlist
            