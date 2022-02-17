class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) == 0:
            return True
        ns = 0
        lr = 0
        moves = moves.lower()
        lm = list(moves)
        for x in lm:
            if x == 'u':
                ns += 1
            if x == 'd':
                ns -= 1
            if x == 'l':
                lr += 1
            if x == 'r':
                lr -= 1
        if ns == 0 and lr == 0:
            return True
        else:
            return False