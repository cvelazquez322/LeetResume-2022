class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        counter = 0
        for i in range(len(startTime)):
            if queryTime in range(startTime[i], endTime[i]) or queryTime == endTime[i]:
                counter += 1
        return counter