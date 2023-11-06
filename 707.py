

class MyLinkdedList(object):

    def __init__(self):
        self.val = 0
        self.next = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self
        for i in range(index) - 1:
            if current.next:
                current = current.next
            else:
                return -1

        return current.val

    def addAtHead(self, val):
        """
        :type val:int
        :rtype: None
        """
        head = MyLinkdedList(val)
        head.next = self

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self
        new_node = MyLinkdedList(val)

        while current.next:
            current = current.next

        current.next = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        current = self.next
        prev = self
        i = 0
        while current:
            if i == index:
                new_node = MyLinkdedList(val)
                prev.next = new_node
                new_node.next = current
                break
            prev = current
            current = current.next
            i += 1
            

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype None
        """
        current = self.next
        prev = self
        i = 0
        while current:
            if i == index:
                prev.next = current.next
                break

# Your MylinkedList object will be instaiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index.val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    solution = Solution()