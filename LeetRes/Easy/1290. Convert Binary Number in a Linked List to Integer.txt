# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def getDecimalHelper(head, valist):
    valist.append(head.val)
    if head.next:
        getDecimalHelper(head.next, valist)
            return valist
def binint(valist):
    bistring = ""
    for x in valist:
        bistring += str(x)
    return int(bistring, 2)
            class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return None
        vlist = []
        vlist = getDecimalHelper(head, vlist)
        return binint(vlist)
                