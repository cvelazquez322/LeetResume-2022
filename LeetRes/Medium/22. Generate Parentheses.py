def checker(s):
    ilist = []
    for item in s:
        if item == '(':
            ilist.append(item)
            continue
        if item == ')' and len(ilist) > 0:
            if ilist[-1] == '(':
                ilist = ilist[:-1]
        else:
            return False
    return len(ilist) == 0
        def gpHelper(num, istr, rlist,r, l):
    if num == 0:
        if checker(istr):
            rlist.append(istr)
        return rlist
    gpHelper(num-1, istr + '(', rlist, r + 1, l)
    if r > l:
        gpHelper(num-1, istr + ')', rlist, r, l + 1)
    return rlist
    class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return gpHelper((n * 2) -1, '(', [], 1, 0)