class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx = list(f'{x:032b}')
        yy = list(f'{y:032b}')
        i = 0
        counter = 0
        while(i < len(xx)):
            if xx[i] != yy[i]:
                counter +=1
            i += 1
        return counter
        