# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur_node = head
        rev_head = None
        
        while cur_node != None:
            new_node = ListNode(cur_node.val)
            new_node.next = rev_head
            rev_head = new_node
            cur_node = cur_node.next
        
        return rev_head
