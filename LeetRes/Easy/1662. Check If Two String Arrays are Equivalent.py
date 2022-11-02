def strMaker(Strlst):
    r = ""
    for x in Strlst:
        r += x
    return r
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = strMaker(word1) 
        str2 = strMaker(word2)
        return str1 == str2