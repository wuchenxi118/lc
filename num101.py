# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        # if not root:
        #     return True
        res = []
        now_queue=[]
        next_queue = []
        queue = []
        queue.append(root)
        while(len(queue)>0):
            now_root = queue[0]
            res.append(now_root.val)
            if now_root.left:
                queue.append(now_root.left)
            if now_root.right:
                queue.append(now_root.right)
            del queue[0]

        print(res)

if __name__ == '__main__':
    root  = TreeNode(0)
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)

    root.left = l1
    root.right = l2
    l1.left = l3
    l3.left = l4

    S = Solution()
    S.isSymmetric(root)


