class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] in [10, 20]:
            return False
                cashr = {}
        cashr[5] = 0
        cashr[10] = 0
        cashr[20] = 0
                while len(bills) != 0:
            if bills[0] == 5:
                cashr[5] += 1
            if bills[0] == 10:
                if cashr[5]:
                    cashr[5] -= 1
                    cashr[10] += 1
                else:
                    return False
            if bills[0] == 20:
                if cashr[10]:
                    cashr[10] -= 1
                    if cashr[5]:
                        cashr[5] -= 1
                        cashr[20] += 1
                    else:
                        return False
                elif cashr[5]:
                    pos = 0
                    while 3 > pos:
                        if cashr[5]:
                            cashr[5] -= 1
                            pos += 1
                        else:
                            return False
                else:
                    return False
            bills.pop(0)
        return True
                                        