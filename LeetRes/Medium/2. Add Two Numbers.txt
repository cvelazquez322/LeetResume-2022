# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def ll2lst(ll, lst):
    lst.append(ll.val)
    if ll.next:
        ll2lst(ll.next, lst)
    return lst
def lst2ll(lst):
    newNode = ListNode(lst.pop(0))
    if lst:
        newNode.next = lst2ll(lst)
    return newNode
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lst1 = ll2lst(l1, [])
        lst2 = ll2lst(l2, [])
        lst1.reverse()
        lst2.reverse()
        s1 = [str(x) for x in lst1]
        s1 = int("".join(s1))
        s2 = [str(x) for x in lst2]
        s2 = int("".join(s2))
        newlli = s2 + s1
        #print(s1, s2, newlli)
        newlll = list(str(newlli))
        newlll.reverse()
        return lst2ll(newlll)
                