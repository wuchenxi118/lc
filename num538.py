from copy import deepcopy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def __init__(self):
#         self.nsum=0
#         self.root = None
#         self.nval = []
#
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root
#         self.front_search(root)
#         self.no2_front_search(root)
#
#         return root
#
#     def no2_front_search(self,node):
#         if node==None:
#             return
#         big_value_list = [i for i in self.nval if i>node.val]
#         node.val+=sum(big_value_list)
#
#         self.no2_front_search(node.left)
#         self.no2_front_search(node.right)
#
#
#     def front_search(self,node):
#         if node==None:
#             return
#         self.nval.append(node.val)
#
#         self.front_search(node.left)
#         self.front_search(node.right)


class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if not root:
            return root
        self.midOrder(root)
        return root

    def midOrder(self,node):
        if node==None:
            return
        self.midOrder(node.right)
        self.total += node.val
        node.val = self.total
        self.midOrder(node.left)




if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)

    S = Solution()
    out_tree = S.convertBST(root)
    print(out_tree.val)
    print(out_tree.left.val)