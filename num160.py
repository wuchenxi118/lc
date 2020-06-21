# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def getIntersectionNode(self, headA, headB):
    #     if not headA or not headB:
    #         return None
    #     save = set()
    #     while headA or headB:
    #         if headA:
    #             if headA in save:
    #                 return headA
    #             else:
    #                 save.add(headA)
    #                 headA = headA.next
    #
    #         if headB:
    #             if headB in save:
    #                 return headB
    #             else:
    #                 save.add(headB)
    #                 headB = headB.next
    #     return None

    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        while pA or pB:

            if pA == pB:
                return pA

            if pA == None:
                pA = headB
            else:
                pA = pA.next

            if pB == None:
                pB = headA
            else:
                pB = pB.next

        return None



