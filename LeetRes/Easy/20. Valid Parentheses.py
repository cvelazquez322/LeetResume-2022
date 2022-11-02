def checker(one, two):
    if one == '[':
        if two == ']':
            return True
    if one == '(':
        if two == ')':
            return True
    if one == '{':
        if two == '}':
            return True
    return False
class Solution:
    def isValid(self, s: str) -> bool:
        llist = []
        for character in s:
            if not llist and character in [']', ')', '}']:
                return False
                        if character in ['(', '[', '{']:
                llist.append(character)
            else:
                if checker(llist[-1], character):
                    llist.pop()
                    continue
                else:
                    return False
        if llist:
            return False
        return True
                