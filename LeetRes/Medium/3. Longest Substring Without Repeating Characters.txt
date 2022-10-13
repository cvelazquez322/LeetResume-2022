def findDup(istring):
    for i in range(len(istring)):
        if istring[i] in istring[i +1:]:
            return istring[i]
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                curr_string = ""
        curr_val, max_val = 0, 0
        i, z = 0, 0
        while i < len(s):
            z = i
            while z < len(s):
                if s[z] in curr_string:
                    curr_string += s[z]
                    duplicate = findDup(curr_string)
                    counter = 0
                    for j in range(len(curr_string)):
                        counter += 1
                        if curr_string[j] == duplicate:
                            curr_string = curr_string[j + 1:]
                            curr_val = len(curr_string)
                            break
                        else:
                            currstring = curr_string[j + 1:]
                    i += counter
                else:
                    curr_string += s[z]
                    curr_val += 1
                    if curr_val > max_val:
                        max_val = curr_val
                z += 1
            i += 1
        return max_val