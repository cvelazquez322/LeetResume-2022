class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        rstring = ''
        carry = 0
        i = 0
        len1 = len(num1) 
        len2 = len(num2)
        maxlen = max(len1, len2)
        while i < maxlen or carry:
            dig1  = int(num1[i]) if i < len1 else 0
            dig2  = int(num2[i]) if i < len2 else 0
            dig3  = (dig1 + dig2 + carry) % 10
            carry = (dig1 + dig2 + carry) // 10
            rstring += str(dig3)
            i    += 1
        return rstring[::-1]