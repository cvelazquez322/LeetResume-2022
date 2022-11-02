class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if len(flowerbed) == 0:
            return 0
        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            if n == 0 and flowerbed[0] == 1:
                return True
            if n == 0 and flowerbed[0] == 0:
                return True
            else:
                return False
        while n != 0:
            if len(flowerbed) == i:
                return False
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i +1] == 0:
                    n -=1
                    flowerbed[i] = 1
                    i += 1
                    continue
            elif i == len(flowerbed) - 1:
                if flowerbed[i- 1] == 0 and flowerbed[i] == 0:
                    n -=1
                    flowerbed[i] = 1
                    i += 1
                    continue
            else:
                if flowerbed[i -1] == 0 and flowerbed [i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                    i += 1
                    continue
            i += 1
        print(flowerbed)
        return True