# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from math import ceil
integer = 0.0
def linkedlistcounter(node):
    if node.next:
        global integer
        integer += 1
        linkedlistcounter(node.next)
    #on final iteration, will not count itself, adds 1
    #to correct this 
    return integer + 1
def numreturned(ll, num):
    num -= 1
    while num != 0:
        return numreturned(ll.next, num)
    if num == 0:
        return ll
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #gets the length of the LL
        count = linkedlistcounter(head)
        global integer
        integer = 0.0
        if count % 2 == 0:
            count += 1
        count = ceil(count/2)
        return numreturned(head, count)
               