"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        n = (l1.val + l2.val)
        
        if n > 9:
            n = n - 10
            flag = 1
        else:
            flag = 0
        h = ListNode(n)
        a = l1
        b = l2
        c = h
        
        while a.next != None:
            a = a.next
            if b.next == None:
                n = a.val
            else:
                b = b.next
                n =(a.val+b.val)
            if flag == 1:
                n = n + 1
            if n > 9:
                n = n- 10
                flag = 1
            else:
                flag = 0
            c.next = ListNode(n)
            c = c.next
        while b.next != None:
            b = b.next
            n = b.val
            if flag == 1:
                n = n + 1
            if n > 9:
                n = n- 10
                flag = 1
            else:
                flag = 0
            c.next = ListNode(n)
            c = c.next
        if flag == 1:
            c.next = ListNode(1)
        return h
                
            
            