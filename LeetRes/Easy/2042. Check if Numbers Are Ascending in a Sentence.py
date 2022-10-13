def sttl(s):
    rlist, ints = [], ''
    for x in s:
        if x.isdecimal():
            ints += x
        elif not x.isdecimal() and ints:
            rlist.append(int(ints))
            ints = ''
    if ints:
        rlist.append(int(ints))
    return rlist
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        llist = sttl(s)
        prev = None
        for x in llist:
            #print(llist)
            if prev:
                if prev >= x:
                    return False
            prev = x
        return True
                                