class Solution:
    # def isValidBST(self, root):
    #     def helper(node,low,high):
    #         if not node:
    #             return True
    #         val = node.val
    #         if val <= low or val >= high:
    #             return False
    #         if not helper(node.right,val,high):
    #             return False
    #         if not helper(node.left,low,val):
    #             return False
    #
    #         return True
    #     return helper(root,-float('inf'),float('inf'))

    def isValidBST(self, root):

        if not root:
            return True

        stack = []
        pre_num = -float('inf')

        while(root or len(stack)>0):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre_num<root.val:
                    pre_num=root.val
                else:
                    return False
                root = root.right
        return True
