class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0
        for x in patterns:
            if x in word:
                counter += 1
        return counter
        