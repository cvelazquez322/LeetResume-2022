def comHelper(digits, total, rlist):
    if digits == '':
        rlist.append(total)
        return
    mapper = {}
    mapper['2'] = ['a', 'b', 'c']
    mapper['3'] = ['d','e','f']
    mapper['4'] = ['g','h','i']
    mapper['5'] = ['j','k','l']
    mapper['6'] = ['m','n','o']
    mapper['7'] = ['p','q','r','s']
    mapper['8'] = ['t', 'u', 'v']
    mapper['9'] = ['w','x','y','z']
    while digits[0] in mapper:
        total += mapper[digits[0]][0]
        comHelper(digits[1:], total, rlist)
        mapper[digits[0]].pop(0)
        total = total [:-1]
        if not mapper[digits[0]]:
            del mapper[digits[0]]
    return rlist
        class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        else:
            return comHelper(digits, '', [])