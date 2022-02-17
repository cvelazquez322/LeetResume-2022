# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def ddHelper(parent, son):
    if son is None:
        return
    if parent:
        if parent.val == son.val:
            parent.next = son.next
            ddHelper(parent, parent.next)
    if son.next:
        ddHelper(son, son.next)
    return son
            class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        return ddHelper(None, head)