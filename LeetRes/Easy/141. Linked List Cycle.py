# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def checker(ll, rmap):
    if ll in rmap:
        return True
    rmap[ll] = True
    if ll.next:
        return checker(ll.next, rmap)
    else:
        return False
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            return checker(head, {})
        else:
            return False