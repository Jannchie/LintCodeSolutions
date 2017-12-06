
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            a = ListNode(l1.val)
            l1 = l1.next
        else:
            a = ListNode(l2.val)
            l2 = l2.next
        while l1 != None or l2 != None:
            temp = a
            while temp.next != None:
                temp = temp.next
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
                if l1 == None:
                    temp.next.next = ListNode(l2.val,l2.next)
                    break
            else :
                temp.next = ListNode(l2.val)
                l2 = l2.next
                if l2 == None:
                    temp.next.next = ListNode(l1.val,l1.next)
                    break
        return a
                
