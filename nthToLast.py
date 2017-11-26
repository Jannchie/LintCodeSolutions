class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLastA(self, head, n):
        # 最开始的想法，超慢。
        while head != None:
            temp = head
            counter = 0
            while counter < n:
                counter += 1
                temp = temp.next
            if temp == None:
                return head
            head = head.next
        return head


    def nthToLastB(self, head, n):
        # 两次遍历，第一次遍历，获得链表长度，第二次遍历，获得指定位置的结点。
        counter = 0
        while head != None:
            counter += 1
            head = head.next
        temp = head
        while counter - n != 0:
            counter -= 1
            temp = temp.next
        return temp
