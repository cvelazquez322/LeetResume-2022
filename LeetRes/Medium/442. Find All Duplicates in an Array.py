class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        emap = {}
        rmap = {}
        tmap = {}
        for x in nums:
            if x not in emap:
                emap[x] = True 
                continue
            if x in emap and x not in tmap:
                rmap[x] = True
                continue
            if x in rmap:
                rmap.pop(x)
                tmap[x] = True
                continue
        return list(rmap)
            