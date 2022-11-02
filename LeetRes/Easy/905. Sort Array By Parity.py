def sHelper(ilist):
    even, odd = [], []
    for item in ilist:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    return even + odd
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sHelper(nums)