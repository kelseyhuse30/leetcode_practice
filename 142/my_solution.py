# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
            
        slow = fast = head
        
        while True:
            slow = slow.next
            
            try:
                fast = fast.next.next
            except:
                return
        
            if fast == slow:
                break
        
        while head != slow:
            head = head.next
            slow = slow.next
        
        return slow
