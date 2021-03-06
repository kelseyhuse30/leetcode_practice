class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        
    def get(self, index):
        # """
        # Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        # :type index: int
        # :rtype: int
        # """
        if index < 0 or index >= self.size:
            return -1
        
        if self.head == None:
            return -1
        
        node = self.head
        for i in range(index):
            node = node.next
        return node.val
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        old_head = self.head
        self.head = Node(val)
        self.head.next = old_head
        self.size += 1
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = self.head
        if node == None:
            self.head = Node(val)
        else:
            while node.next != None:
                node = node.next
            node.next = Node(val)
        self.size += 1
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            if 0 < index < self.size:
                node = self.head
                for i in range(index - 1):
                    node = node.next
                new_node = Node(val)
                new_node.next = node.next
                node.next = new_node
                self.size += 1
            
    def deleteAtIndex(self, index):
        # """
        # Delete the index-th node in the linked list, if the index is valid.
        # :type index: int
        # :rtype: void
        # """
        if 0 < index < self.size:
            node = self.head
            for i in range(index - 1):
                node = node.next
            if node.next.next != None:
                node.next = node.next.next
            else:
                node.next = None
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
