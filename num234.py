# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res_list = []
        if not head:
            return True
        while(head):
            res_list.append(head.val)
            head = head.next

        if len(res_list)==1:
            return True

        if len(res_list)%2 == 0:
            print('t')
            res_2 = res_list[len(res_list)//2:]
            print(res_2)
            res_2 = res_2[::-1]
            print(res_2)
            print(res_list[:len(res_list)])
            if res_2 == res_list[:len(res_list)//2]:

                return True
            else:
                return False

        if len(res_list) % 2 == 1:
            res_2 = res_list[len(res_list) // 2+1:]
            print(res_2)
            res_2 = res_2[::-1]
            if res_2 == res_list[:len(res_list)//2]:

                return True
            else:
                return False


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(0)
    a.next.next = ListNode(1)
    S = Solution()
    print(S.isPalindrome(a))

