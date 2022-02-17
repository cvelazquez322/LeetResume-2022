class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pos = 0
        lenarr = len(arr)
        if lenarr == 0:
            return []
        while lenarr > pos:
            if arr[pos] == 0:
                arr.pop(lenarr - 1)
                arr.insert(pos, 0)
                pos += 1
            pos += 1
        return
                