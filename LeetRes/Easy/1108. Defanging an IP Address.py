class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = list(address)
        i = 0
        s = ""
        if len(address) == 0:
            return []
        while len(address) > i:
            if address[i] == '.':
                address[i] = '[.]'
            i += 1
        s = s.join(address)
        return s