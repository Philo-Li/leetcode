# given the head of a linked list and an integer val,
# remove all the nodes of the linkded list that has Node.val == val
# and return the new head
# Definition for singly-linkded list.
# class ListNode(object):
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElement(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # create virtual head node
        dummy_head = ListNode(next = head)

        # traverse the list and delete the node which value equals val
        current = dummy_head
        while current.next:
            # print(current.next.val)
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement(ListNode([]), 1))
    print(solution.removeElement(ListNode([7, 7, 7, 7]), 7))
    print(solution.removeElement(ListNode([1, 2, 6, 3, 4, 5, 6]), 6))
