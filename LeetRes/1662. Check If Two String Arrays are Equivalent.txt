def strMaker(Strlst):
    r = ""
    for x in Strlst:
        r += x
    return r
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = strMaker(word1) 
        str2 = strMaker(word2)
        if len(str1) != len(str2):
            return False
        x = 0
        while x < len(str1):
            if str1[x] != str2[x]:
                return False
            x += 1
        return True