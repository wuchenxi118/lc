# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.stack = []
        self.res = []
    def inorderTraversal(self, root):
        if root==None:
            return self.res

        while (root or len(self.stack)>0):
            # print(root.val)
            if root:
                self.stack.append(root)
                root = root.left
            else:
                root = self.stack.pop()
                self.res.append(root.val)
                root = root.right
        return self.res

    def postorderTraversal(self, root):
        if root==None:
            return self.res
        while(root or len(self.stack)>0):
            while()





if __name__ == '__main__':
    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)

    root.left = l2
    root.right = l3



    l2.left = l4
    l2.right = l5

    l3.left = l6
    S = Solution()
    print(root)
    print(S.inorderTraversal(root))
