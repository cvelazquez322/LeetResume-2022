# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def helper(curr, rlist):
    rlist.append(curr.val)
    if curr.next:
        helper(curr.next, rlist)
    return rlist
                    class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ilist = helper(head, [])
        maxS = ilist[0] + ilist[-1]
        r, l = 1, len(ilist) - 2 
        while r < l:
            maxS = max(maxS, ilist[r] + ilist[l])
            r +=1
            l -= 1
        return maxS
        