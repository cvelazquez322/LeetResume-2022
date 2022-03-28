class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldierMap, rlist = {}, []
        for i in range(len(mat)):
            soldierCounter = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    soldierCounter += 1
                                if soldierCounter in soldierMap: 
                soldierMap[soldierCounter].append(i)
            else:
                soldierMap[soldierCounter] = [i]
                                while len(rlist) < k:
            rlist += soldierMap[min(soldierMap)]
            del soldierMap[min(soldierMap)]
                rlist = rlist[:k]
                    return rlist
                        