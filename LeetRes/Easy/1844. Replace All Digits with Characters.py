class Solution:
    def replaceDigits(self, s: str) -> str:
        newS, currL = '', ''
        for i in range(len(s)):
            #print(newS)
            if s[i].isdecimal():
                newL = chr(ord(currL) + int(s[i]))
                newS += newL
            else:
                newS += s[i]
                currL = s[i]
        return newS
        