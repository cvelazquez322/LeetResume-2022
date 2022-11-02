def sHelper(ilist, rmap, depth):
    imap = {}
    for item in ilist[0]:
        if depth == 0:
            imap[item] = 1
        else:
            if item in rmap:
                imap[item] = 1
    del ilist[0]
    if ilist:
        return sHelper(ilist, imap, depth + 1)
        return imap
    class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        imap = sHelper(nums, {}, 0)
        rlist = []
        while imap:
            rlist.append(min(imap))
            del imap[min(imap)]
        return rlist