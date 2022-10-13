def row(imatrix, target):
    try:
        for i in range(len(imatrix)):
            if target >= imatrix[i][0] and target < imatrix[i +1][0]:
                return i
        return i
    except:
        return i
    def finder(ilist, target):
    for i in range(len(ilist)):
        if ilist[i] == target:
            return True
    return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        poss = row(matrix, target)
        return finder(matrix[poss], target)