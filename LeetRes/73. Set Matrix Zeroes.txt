def findzeros(matrix):
    rlist = []
    for  yaxis in range(len(matrix)):
        for xindex in range(len(matrix[yaxis])):
            if matrix[yaxis][xindex] == 0:
                rlist.append([yaxis,xindex])
    return rlist
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = findzeros(matrix)
        for corodinates in zeros:
            i = 0
            #print(zeros, corodinates)
            while i < len(matrix):
             #   print(matrix, 'first loop', i)
                matrix[i][corodinates[1]] = 0
                i += 1
            i = 0
            while i < len(matrix[0]):
              #  print(matrix, 'second loop')
                matrix[corodinates[0]][i] = 0
                i += 1
        #print(matrix)