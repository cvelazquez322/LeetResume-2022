class Solution:
    def countTriples(self, n: int) -> int:
        numlist, mapper, counter = [], {}, 0
        for i in range(1, n + 1):
            numlist.append(i * i)
            mapper[i *i] = 1
        for i in range(len(numlist)):
            j = i + 1
            while j < len(numlist):
                if numlist[i] + numlist[j] in mapper:
                    counter += 1
         #           print(numlist[i], numlist[j])
                j += 1
        #print(mapper, numlist)
        return counter * 2
                