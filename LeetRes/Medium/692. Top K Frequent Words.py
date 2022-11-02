def counter(words):
    rmap = {}
    for item in words:
        if item in rmap:
            rmap[item] += 1
        else:
            rmap[item] = 1
    return rmap
def inverter(words):
    rmap = {}
    for item in words:
        if words[item] in rmap:
            rmap[words[item]].append(item)
            rmap[words[item]].sort()
        else:
            rmap[words[item]] = [item]
    return rmap
def converter(words, num):
    rlist = []
    while num > 0:
        for item in words[max(words)]:
            rlist.append(item)
        num -= len(words[max(words)])
        del words[max(words)]
    while num < 0:
        rlist = rlist[:-1]
        num += 1
    return rlist
        class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return converter(inverter(counter(words)), k)
        