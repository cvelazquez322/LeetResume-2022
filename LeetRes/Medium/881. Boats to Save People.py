class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        bcounter = 0
        l, r = 0, len(people) -1
        while l <= r:
            if l == r:
                bcounter+= 1
                break
            if people[l] + people[r] <= limit:
                l, r = l+1, r-1
                bcounter += 1
            else:
                r -= 1
                bcounter += 1
        return bcounter