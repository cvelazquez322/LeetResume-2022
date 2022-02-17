class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first, second, third = 'qwertyuiopQWERTYUIOP', "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"
        rlist = []
        for word in words:
            one, two, three = 1, 1, 1
            for letter in word:
                #print(letter, word)
                if letter not in first:
                    one = 0
                if letter not in second:
                    two = 0
                if letter not in third:
                    three = 0
                if not one and not two and not three:
                    continue
            if one or two or three:
                rlist.append(word)
        return rlist