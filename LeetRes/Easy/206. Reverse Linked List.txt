# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def rlHelper(head, rlist):
    rlist.append(head.val)
    if head.next:
        rlHelper(head.next, rlist)
        return rlist
def ltoll(llist):
    newnode = ListNode(llist[0])
    llist.pop(0)
    if len(llist) != 0:
        newnode.next = ltoll(llist)
    return newnode
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        rlist = rlHelper(head, [])
        rlist.reverse()
        return ltoll(rlist)
                