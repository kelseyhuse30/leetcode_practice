class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # must traverse list using 'next'
        cur = self.head
        end = False
        i = 0
        while cur.next != None:
            if i == index:
                end = True
                break
            i += 1
            cur = cur.next
        if end == True:
            return cur.val
        else:
            return -1
              

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        cur = self.head
        self.head = Node(val)
        self.head.next = cur
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        cur = self.head
        i = 0
        while cur.next != None:
            prev = cur
            cur = cur.next
            i += 1
            if i == index:
                new_node = Node(val)
                new_node.next = cur
                prev.next = new_node
                break     

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        cur = self.head
        i = 0
        while cur.next != None:
            prev = cur
            cur = cur.next
            i += 1
            if i == index:
                prev.next = cur.next
                break       


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
