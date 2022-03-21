def findDup(istring):
    for i in range(len(istring)):
        if istring[i] not in istring[i +1:] and istring[i] not in istring[:i]:
            return i
    return -1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return findDup(s)