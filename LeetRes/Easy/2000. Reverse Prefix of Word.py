class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        newS, counter = '', 0
        for letter in word:
            if letter == ch:
                newS += letter
                newS = newS[::-1] + word[counter + 1:]
                break
            else:
                newS += letter
                counter += 1
        return newS