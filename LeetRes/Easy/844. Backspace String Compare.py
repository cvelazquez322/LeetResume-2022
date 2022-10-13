def remover(s):
    newS = ''
    for letter in s:
        if letter == '#':
            newS = newS[:-1]
        else:
            newS += letter
    return newS
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return remover(s) == remover(t)
        