class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        S = list(S)
        J = list(J)
        for x in S:
            if x in J:
                counter += 1
        return counter