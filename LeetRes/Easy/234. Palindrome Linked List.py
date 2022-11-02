# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def helper(root, rlist):
    rlist.append(root.val)
    if root.next:
        helper(root.next, rlist)
    return rlist
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ilist = helper(head, [])
        r, l = 0, len(ilist) - 1
        while r < l:
            if ilist[r] != ilist[l]:
                return False
            r,l = r+1, l -1
        return True
        