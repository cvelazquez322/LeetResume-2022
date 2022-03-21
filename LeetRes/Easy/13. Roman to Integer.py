class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.lower()
        part = list(s)
        it = 0
        total = 0
        while it < len(part):
            if part[it] == 'i' and (len(part) -it >= 2):
                if part[it + 1] == 'v':
                    total += 4
                    it += 2
                    continue
                elif part[it + 1] == 'x':
                    total += 9
                    it += 2
                    continue
                          if part[it] == 'x' and (len(part) -it >= 2):
                if part[it + 1] == 'l':
                    total += 40
                    it += 2
                    continue
                elif part[it + 1] == 'c':
                    total += 90
                    it += 2
                    continue
                            if part[it] == 'c' and (len(part) -it >= 2):
                if part[it + 1] == 'd':
                    total += 400
                    it += 2
                    continue
                elif part[it + 1] == 'm':
                    total += 900
                    it += 2
                    continue
                           if part[it] == 'v':
                total += 5
            if part[it] == 'l':
                total += 50
            if part[it] == 'd':
                total += 500
            if part[it] == 'm':
                total += 1000
            if part[it] == 'i':
                total += 1
            if part[it] == 'x':
                total += 10
            if part[it] == 'c':
                total += 100
                        it += 1
                return total