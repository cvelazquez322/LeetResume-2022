# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def helper(head, rlist, total):
    if head.val == 0 and total != 0:
        rlist.append(total)
        total = 0
    total += head.val
    if head.next:
        helper(head.next, rlist, total)
    return rlist
def llMaker(ilist):
    newNode = ListNode(ilist[0])
    del ilist[0]
    if ilist:
        newNode.next = llMaker(ilist)
    return newNode
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
                headVals = helper(head, [], 0)
                return llMaker(headVals)