def stinc(ilist):
    try:
        for i in range(len(ilist)):
            if ilist[i] >= ilist[i+1]:
                return i
    except:
        return i
    def stdec(ilist):
    try:
        for i in range(len(ilist)):
            if ilist[i] <= ilist[i+1]:
                return i
    except:
        return i
    class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or stdec(arr) == len(arr) -1 or stinc(arr) == len(arr) - 
            1:
            return False
        index = stinc(arr)
        index += stdec(arr[index:])
        if index == len(arr) - 1:
            return True
        return False