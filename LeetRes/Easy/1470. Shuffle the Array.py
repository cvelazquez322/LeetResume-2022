class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nNums = []
        for i in range(int(len(nums)/2)):
            nNums.append(nums[i])
            nNums.append(nums[i+ n])
        return nNums