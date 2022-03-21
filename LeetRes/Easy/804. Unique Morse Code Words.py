class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        vlist = []
        olist = []
        maps = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-"
            ,".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-","
            .--","-..-","-.--","--.."]
        for x in words:
            estring = ""
            for y in x:
                estring += (maps[ord(y) - 97])
            olist.append(estring)
        for x in olist:
            if x in vlist:
                continue
            else:
                vlist.append(x)
        return len(vlist)
                        