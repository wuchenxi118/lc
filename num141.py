# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or head.next==None:
            return False
        node_list = []
        while(head):
            if head not in node_list:
                node_list.append(head)
            else:
                return True
            head = head.next
        return False

    def hasCycle2(self, head):
        if not head or head.next==None:
            return False
        slow = head
        fast = head.next
        while(slow!=fast):
            if fast==None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

