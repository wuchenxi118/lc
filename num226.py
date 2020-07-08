# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        node = root
        self.dfs(node)

        return root
    def dfs(self,node):
        if not node:
            return
        temp = node.left
        node.left = node.right
        node.right = temp

        self.dfs(node.left)
        self.dfs(node.right)