class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        news, ogLen = '', len(s)
        i = 0
        while (i < ogLen) and s:
            if i % 2 == 0:
                news += s[:k][::-1]
            else:
                news += s[:k]
            s = s[k:]
            i += 1
        return news
            