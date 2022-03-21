class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cursum = 0
        for x in operations:
            if x.lower() == "x++" or x.lower() == "++x":
                cursum += 1
            else:
                cursum -= 1
        return cursum