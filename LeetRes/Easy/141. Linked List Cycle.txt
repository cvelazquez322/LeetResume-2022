# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def helper(head, llist):
    if head in llist:
        return True
    llist[head] = True
    if head.next:
        return helper(head.next, llist)
    return False
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        return helper(head, {})