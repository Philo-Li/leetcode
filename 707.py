class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Single LinkedList
# set a virtual head node
class MyLinkdedList(object):
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if  index < 0 or index >= self.size:
            return -1

        current = self.dummy_head.next
        for i in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val):
        """
        :type val:int
        :rtype: None
        """
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.dummy_head

        while current.next:
            current = current.next

        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
       
        current = self.dummy_head
        for i in range(index):
            current = current.next
        
        current.next = ListNode(val, current.next)
        self.size += 1
            

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype None
        """
        if index < 0 or index >= self.size:
            return
        
        current = self.dummy_head
        for i in range(index):
            current = current.next

        current.next = current.next.next
        self.size -= 1

# Your MylinkedList object will be instaiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index.val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    solution = Solution()