# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def mergeHelper(l1, l2, combo):
    if l1 and l2:
        if l1.val >= l2.val:
            combo = ListNode(l2.val)
            combo.next = mergeHelper(l1, l2.next, None)
        if l1.val < l2.val:
                        combo = ListNode(l1.val)
            combo.next = mergeHelper(l1.next, l2, None)
                                    elif l1:
        combo = ListNode(l1.val)
        combo.next = mergeHelper(l1.next, None, None)
    elif l2:
        combo = ListNode(l2.val)
        combo.next = mergeHelper(None, l2.next, None)
    return combo
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return mergeHelper(l1, l2, None)
                                                                            