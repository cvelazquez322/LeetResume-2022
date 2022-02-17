class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        thePack = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                thePack.append("FizzBuzz")
                        elif i % 3 == 0:
                thePack.append("Fizz")
                            elif i % 5 == 0:
                thePack.append("Buzz")
                    else:
                thePack.append(str(i))
        return thePack