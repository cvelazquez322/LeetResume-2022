def helper(node, rmap):
    if node in rmap:
        return node
    else:
        rmap[node] = node
    if node.next:
        return helper(node.next, rmap)
    return None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return helper(head, {})