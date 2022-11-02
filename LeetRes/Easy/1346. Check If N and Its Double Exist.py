class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lmap = {}
        for x in arr:
            if 2 * x in lmap or x / 2 in lmap:
                return True
            if x not in lmap:
                lmap[x] = 1
        return False
                    