# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        if head.next == None:
            return head
        
        odd_head = cur_odd = head
        even_head = cur_even = head.next

        while cur_odd.next != None and cur_even.next != None:
            if cur_odd.next.next != None:
                cur_odd.next = cur_odd.next.next
                cur_odd = cur_odd.next
            if cur_even.next.next != None:
                cur_even.next = cur_even.next.next
                cur_even = cur_even.next
        
        cur_odd.next = even_head
        cur_even.next = None
        
        return odd_head
