class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rmap = {}
        for i in range(len(list1)):
            counter = 0
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j in rmap:
                        rmap[i + j].append(list1[i])
                    else:
                        rmap[i + j] = [list1[i]]
                    break
        return rmap[min(rmap)]