class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        case1, case2, case3 = True, True, True
        capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                for i in range(len(word)):
            if word[i] not in capitals:
                case1 = False
            if word[i] in capitals:
                case2 = False
            if i == 0:
                if word[i] not in capitals:
                    case3 = False
            elif word[i] in capitals:
                case3 = False
        return case1 or case2 or case3