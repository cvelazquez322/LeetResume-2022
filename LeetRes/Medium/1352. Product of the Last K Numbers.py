class ProductOfNumbers:
    def __init__(self):
        self.array = []
        self.dict = {}
                    def add(self, num: int) -> None:
        self.array.append(num)
        self.dict = {}
                    def getProduct(self, k: int) -> int:
        newArray = self.array[-k:]
        prod = 1
        if k not in self.dict:
            for item in newArray:
                prod *= item
            self.dict[k] = prod
            return prod
        else:
            return self.dict[k]
        # Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)