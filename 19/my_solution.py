# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 1
        cur = head
        
        while cur.next != None:
            cur = cur.next
            length += 1
        
        index = length - n
        cur_index = 0
        cur = head
        
        if index == 0:
            return head.next
        
        while cur_index < index - 1:
            cur = cur.next
            cur_index += 1
            
        cur.next = cur.next.next
        
        return head
