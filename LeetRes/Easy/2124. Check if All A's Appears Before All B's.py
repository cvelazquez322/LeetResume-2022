class Solution:
    def checkString(self, s: str) -> bool:
        mapper = {}
        for x in s:
            if 'b' in mapper and x == 'a':
                return False
                        else:
                mapper[x] = 1
                    return True