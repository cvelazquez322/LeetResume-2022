class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rlist = []
        while len(rlist) < len(matrix[0]):
                rlist.append([])
        for row in matrix:
            i = 0
            for item in row:
                rlist[i].append(item)
                i += 1
        return rlist
                        