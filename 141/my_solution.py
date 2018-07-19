# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
            
        slow = head
        fast = head
        
        while True:
            slow = slow.next
            
            if fast.next != None:
                fast = fast.next.next
            else:
                return False
            
            if slow == None or fast == None:
                return False
            
            if slow == fast:
                return True
