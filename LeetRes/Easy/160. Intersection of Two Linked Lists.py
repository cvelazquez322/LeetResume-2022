# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def helper(r1, r2, imap):
    c1, c2 = 1, 1
    while c1 or c2:
        if r1 in imap and c1:
            return r1
        else:
            imap[r1] = True
        if r2 in imap and c2:
            return r2
        else:
            imap[r2] = True
                                if r1.next:
            r1 = r1.next
        else:
            c1 = 0
        if r2.next:
            r2 = r2.next
        else:
            c2 = 0
                return None
                class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        return helper(headA,headB, {})
                