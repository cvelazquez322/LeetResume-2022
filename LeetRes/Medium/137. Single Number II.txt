class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #note, you have written another code below which ran just a little slower
        # was more memory efficent though
                if len(nums) == 0:
            return []
        odict = {}
        tdict = {}
        for x in nums:
            if x not in odict and x not in tdict:
                odict[x] = True
            elif x in odict and x not in tdict:
                odict.pop(x)
                tdict[x] = True
            else:
                continue
        for x in odict:
            return x
                                                                #if len(nums) == 0:
        #    return []
        #nums.sort()
        #pos = 0
        #while len(nums) > pos + 1: 
        #    if nums[pos] == nums[pos+1]:
        #        pos += 3
        #    else:
        #        return nums[pos]
        #return nums[-1]
                            #rmap = {}
        #tmap = {}
        #for x in nums:
        #    if x not in rmap and x not in tmap:
        #        rmap[x]= True
        #    else:
        #        tmap[x] = True
        #        if x in rmap:
        #            rmap.pop(x)
        #for x in rmap:
        #    return x
        