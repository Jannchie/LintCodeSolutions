"""
Definition of ListNode
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head == None:
            return None
        if head.next == None:
            return head
        pre = head
        now = pre.next
        nex = now.next
        head.next = None
        while True:
            now.next = pre
            if nex == None:
                return now
            pre = now
            now = nex
            nex = nex.next

c = ListNode('c')
b = ListNode('b',next = c)
a = ListNode('a',next = b)
s = Solution()
a = s.reverse(a)
a


