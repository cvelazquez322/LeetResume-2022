class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        prev, counter = 0, 0
        for x in s:
            if prev == '1' and x == '1':
                continue
            if x == '1':
                counter += 1
            prev = x
        return counter == 1