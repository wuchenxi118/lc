#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        Node_list = []
        while(head):
            Node_list.append(head.val)
            head = head.next

        new_head = ListNode(Node_list[-1])
        Node = new_head
        for i in range(len(Node_list)-2,-1,-1):
            Node.next = ListNode(Node_list[i])
            Node = Node.next

        return new_head






if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)

    S = Solution()
    new_head = S.reverseList(a)
    while(new_head):
        print(new_head.val)
        new_head =new_head.next