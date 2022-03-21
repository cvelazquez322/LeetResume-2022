def palindrome(istring):
    l = 0
    r = -1
    while l < len(istring)//2:
        if istring[l] == istring[r]:
            l += 1
            r -= 1
        else:
            return False
    return True
def all_partitions(string):
    for cutpoints in range(1 << (len(string)-1)):
        result = []
        lastcut = 0
        for i in range(len(string)-1):
            if (1<<i) & cutpoints != 0:
                result.append(string[lastcut:(i+1)])
                lastcut = i+1
        result.append(string[lastcut:])
        yield result
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rlist = []
        for partition in all_partitions(s):
            counter = 0
            for substring in partition:
                if palindrome(substring):
                    counter += 1
                if counter == len(partition):
                    rlist.append(partition)
        return rlist