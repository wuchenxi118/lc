from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.fa = {}
        self.vis = defaultdict(int)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.fa[root.val] = None
        self.dfs(root)
        while(p):
            self.vis[p.val] = True
            p = self.fa[p.val]

        while(q):
            if self.vis[q.val]:
                return q
            q = self.fa[q.val]
        return TreeNode(None)

    def dfs(self,root):
        if  root.left:
            self.fa[root.left.val] = root
            self.dfs(root.left)

        if  root.right:
            self.fa[root.right.val] = root
            self.dfs(root.right)

if __name__ == '__main__':
    S = Solution()
    root = TreeNode(10)
    root20 = TreeNode(20)
    root30 = TreeNode(30)
    root.left = root20
    root.right = root30
    print(S.lowestCommonAncestor(root,root20,root30))

