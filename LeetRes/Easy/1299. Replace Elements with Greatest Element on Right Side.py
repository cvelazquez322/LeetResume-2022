def reHelper(arr):
    rlist = []
    pos = 0
    while(len(arr) > pos + 1):
        temp = max(arr[pos + 1:])
        rlist.append(temp)
        pos += 1
    rlist.append(-1)
    return rlist
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        return reHelper(arr)