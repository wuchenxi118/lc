# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     while(root):
    #         if root.left==None:
    #             root = root.right
    #         else:
    #             pre = root.left
    #             while(pre.right):
    #                 pre = pre.right
    #             pre.right = root.right
    #             root.right = root.left
    #             root.left = None
    #             root = root.right

    def flatten(self,root):
        stack = []
        res = []
        node = root
        while(node or len(stack)>0):
            if node:
                res.append(node)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

        for i in range(1,len(res)):
            node = res[i-1]
            node.left=None
            node.right=res[i]

        # return res

    def flatten2(self,root):
        res = []
        def digui(node):
            if node:
                res.append(node)
                digui(node.left)
                digui(node.right)
            else:
                return
        digui(root)
        for i in range(1,len(res)):
            node = res[i-1]
            node.left=None
            node.right=res[i]




if __name__ == '__main__':

    root = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    l7 = TreeNode(7)

    root.left = l2
    root.right = l3
    l2.left = l4
    l2.right = l5
    l4.left = l7
    l3.right = l6

    S =Solution()
    print(S.flatten2(root))
