def helper(s1,s2):
    diff, dlist = 0, []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else:
            diff += 1
            dlist.append(i)
    if diff == 2:
        return s1[dlist[0]] + s1[dlist[1]] == s2[dlist[1]] + s2[dlist[0]]
    if diff == 0:
        return True
    else:
        return False
                    class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2):
            return helper(s1, s2)
        else:
            return False
        