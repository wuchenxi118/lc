# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head or head.next == None:
            return None
        node_list = set()
        while (head):
            if head not in node_list:
                node_list.add(head)
            else:
                return head
            head = head.next
        return None