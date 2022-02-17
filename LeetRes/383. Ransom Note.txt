class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lmag = list(magazine)
        for x in ransomNote:
            if x in lmag:
                lmag.remove(x)
            else:
                return False
        return True