# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def helper(root, counters):
    if root.next:
        counters[0] += 1
        helper(root.next, counters)
        else:
        counters[1] = counters[0]// 2 + 1
        counters[1] -= 1
        if counters[1] == 0:
        counters[0] = root
        return counters[0]
                            class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        return helper(head, [0,-1])