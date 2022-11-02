class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mapper = {}
        for edgeList in edges:
            for edge in edgeList:
                if edge in mapper:
                    mapper[edge] += 1
                else:
                    mapper[edge] = 1
                for x in mapper:
            if mapper[x] == len(edges):
                return x