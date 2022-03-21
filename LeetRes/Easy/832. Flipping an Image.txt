class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()
        z = []
        for i in A:
            c = []
            for b in i:
                print(b)
                if b == 0:
                    c.append(1)
                else:
                    c.append(0)
            z.append(c)
        return z