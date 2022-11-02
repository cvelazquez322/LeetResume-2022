class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = {}
        for i in range(1, n + 1):
            trustMap[i] = [0, 0]
                    for tPath in trust:
            trustMap[tPath[0]][1] += 1
            trustMap[tPath[1]][0] += 1
                for person in trustMap:
            if trustMap[person][0] == n - 1 and trustMap[person][1] == 0:
                return person
                    return -1