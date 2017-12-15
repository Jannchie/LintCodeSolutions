class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        temp = head
        while head != None:
            while head.next != None and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return temp
