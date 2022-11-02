def h1(ilist, k):
    rlist = []
    for i in range(len(ilist)):
        newList = ilist[i + 1:] + ilist[:i]
        rlist.append(sum(newList[:k]))
    return rlist
def h2(ilist, k):
    rlist = []
    for i in range(len(ilist)):
        newList = ilist[i + 1:] + ilist[:i]
        newList = newList[::-1]
        rlist.append(sum(newList[:k * -1]))
    return rlist
def h3(ilist):
    rlist = []
    for i in ilist:
        rlist.append(0)
    return rlist
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k > 0:
            return h1(code, k)
        if k < 0:
            return h2(code, k)
        if k == 0:
            return h3(code)
        