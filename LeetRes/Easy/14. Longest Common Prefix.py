class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        confirmed, possible = '', ''
        while i < len(max(strs)):
            try:
                possible = strs[0][i]
                for x in strs[1:]:
                    if possible != x[i]:
                        return confirmed
                confirmed += strs[0][i]
                i += 1
            except:
                return confirmed
        return confirmed    
                