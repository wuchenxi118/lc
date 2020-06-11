# Definition for a binary tree node.
from copy import deepcopy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        now_queue = []
        next_queue = []
        res = []
        mini_res = []
        now_queue.append(root)

        while(len(now_queue)>0):
            root = now_queue[0]
            del now_queue[0]
            mini_res.append(root.val)

            if root.left:
                next_queue.append(root.left)

            if root.right:
                next_queue.append(root.right)

            if len(now_queue)==0:
                res.append(mini_res)
                mini_res = []
                now_queue = next_queue
                next_queue = []

        return res
    #

    def isSymmetric(self, root):
        root_cp = deepcopy(root)
        return self.check(root,root_cp)

    def check(self,node,node_cp):
        if not node and not node_cp:
            return True
        if not node or not node_cp:
            return False

        return node.val==node_cp.val and self.check(node.left,node_cp.right) and self.check(node.right,node_cp.left)





if __name__ == '__main__':
    root = TreeNode(0)
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)

    root.left = l1
    root.right = l2
    l1.left = l3
    l3.left =l4

    S = Solution()
    print(S.isSymmetric(root))