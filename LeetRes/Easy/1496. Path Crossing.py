class Solution:
    def isPathCrossing(self, path: str) -> bool:
        rmap = {}
        x, y = 0,0
        rmap[x] = {y: False}
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            else:
                print('not valid')
                        if x in rmap:
                if y in rmap[x]:
                    return True
                else:
                    rmap[x][y] = False
            else:
                rmap[x] = {y :False}
        return False