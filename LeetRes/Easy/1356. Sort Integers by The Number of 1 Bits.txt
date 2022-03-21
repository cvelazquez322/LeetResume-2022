#takes a list of ints returns a list binary
#takes a list of ints returns a list binary
def int2bin(arr):
    rlist = []
    for x in arr:
        rlist.append(bin(x)[2:])
    return rlist
#takes a list of binary, sorts it
def sorter(arr):
    rlist = []
    ilist = []
    clist = []
    for x in arr:
        ilist.append(list(x))
    for bilist in ilist:
        counter = 0
        for bi in bilist:
            if bi == "1":
                counter += 1
        clist.append([counter, len(bilist), bilist])
    clist.sort()
    for item in clist:
        rlist.append(item[2])
    return rlist
#takes a list of string, returns int
def bin2int(arr):
    rlist = []
    binlist = []
    s = ''
    for x in arr:
                s = s.join(x)
                binlist.append(s)
        s = ''
    for x in binlist:
        rlist.append(int(x, 2))
    return rlist
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return 0
        rlist = []
        rlist = int2bin(arr)
        rlist = sorter(rlist)
        rlist = bin2int(rlist)
        return rlist
        