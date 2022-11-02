class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lmap, invlmap,rlist = {}, {}, []
        for number in nums:
            if number in lmap:
                lmap[number] += 1
            else:
                lmap[number] = 1
        for x in lmap:
            if lmap[x] in invlmap:
                invlmap[lmap[x]].append(x)
            else:
                invlmap[lmap[x]] = [x]
                for i in range(min(k, len(invlmap))):
            tmpMax = max(invlmap)
            rlist += invlmap[tmpMax]
            del invlmap[tmpMax]
        rlist = rlist[:k]
        return rlist