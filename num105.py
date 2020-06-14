class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        index = {element: i for i, element in enumerate(inorder)}
        n = len(preorder)
        return self.myBuildTree(0,n-1,0,n-1,index,preorder,inorder)


    def myBuildTree(self,preorder_left,preorder_right,inorder_left,inorder_right,index,preorder,inorder):
        if preorder_left>preorder_right:
            return None
        preorder_root = preorder_left
        inorder_root = index[preorder[preorder_root]]
        root = TreeNode(preorder[preorder_root])
        size_left_subtree = inorder_root - inorder_left
        root.left = self.myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1,index,preorder,inorder)
        root.right = self.myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right,index,preorder,inorder)
        return root



