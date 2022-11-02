class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphaDict = {}
        for letter in sentence:
            if letter in alphaDict:
                continue
            else:
                alphaDict[letter] = True
        return len(alphaDict) == 26