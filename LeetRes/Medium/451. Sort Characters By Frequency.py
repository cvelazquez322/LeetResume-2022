class Solution:
    def frequencySort(self, s: str) -> str:
        lmap, inverse, rstring = {}, {}, ''
        for i in s:
            if i in lmap:
                lmap[i] += 1
            else:
                lmap[i] = 1
        for x in lmap:
            if lmap[x] in inverse:
                inverse[lmap[x]] += x
            else:
                inverse[lmap[x]] = x
        for i in range(max(inverse), min(inverse) - 1, -1):
            try:
                if len(inverse[i]) > 1:
                    fullstr = inverse[i]
                    for j in range(len(fullstr)):
                        poss = fullstr[j] * i
                        rstring += poss
                else:      
                    poss = inverse[i] * i
                    rstring += poss
                            except:
                continue
                    return rstring
                    