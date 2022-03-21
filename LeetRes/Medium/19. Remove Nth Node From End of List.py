# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def linkedlength(head, rlist):
    rlist[0] += 1
    if head.next:
        linkedlength(head.next, rlist)
    return rlist[0]
                def helper(head, parent, target):
   # print(target)
    if target == 0:
        if parent and head:
            if head.next:
                parent.next = head.next
                head = None
                return
                        else:
                parent.next = None
                head = None
                return
                        if head:
            if head.next:
                head = head.next
                return head
            head = None
            return head
        if head.next:
        helper(head.next, head, target - 1)
        return head
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> 
        Optional[ListNode]:
        if head is None:
            return None
                target = linkedlength(head, [0])
                return helper(head, None, target - n)
        