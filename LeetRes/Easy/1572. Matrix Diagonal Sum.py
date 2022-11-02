def dia(mat):
    coorMap, x, y, cSum = {}, 0,0, 0
    while True:
        try:
            if mat[x- 1:]:
                if mat[x][y-1:]:
                    if (x,y) in coorMap:
                        x+= 1
                        y += 1
                        continue
                    cSum += mat[x][y]
                    coorMap[(x,y)] = 1
                else:
                    break
            else:
                break
            x += 1
            y += 1
        except:
            break
    x, y = 0, len(mat[0]) -1
    while True:
        try:
            if mat[x- 1:]:
                if mat[x][:y+1]:
                    if (x,y) in coorMap:
                        x+= 1
                        y -= 1
                        continue
                    cSum += mat[x][y]
                    coorMap[(x,y)] = 1
                else:
                    break
            else:
                break
            x += 1
            y -= 1
        except:
            break
    return cSum
            class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 0:
            return 0
        return dia(mat)
        