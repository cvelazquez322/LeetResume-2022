class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        imap = {}
        for item in s:
            if item in imap:
                imap[item] += 1
            else:
                imap[item] = 1
        print(imap)
        for item in t:
            if item in imap:
                imap[item] -= 1
            else:
                return False
            if imap[item] == 0:
                del imap[item]
        return not bool(imap)
            