class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binaryStr = bin(n)[2:]
        newstr = ''
        for x in binaryStr:
            if x is '1':
                newstr +='0'
            else:                                
                newstr +='1'
        return int(newstr,2)