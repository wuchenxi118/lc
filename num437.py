class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.str_ser = ""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.front_search(root)
        return self.str_ser


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_array = data.split(',')
        root = self.rdeserialize(data_array)
        return root

    def rdeserialize(self,l):
        if l and l[0]=='None':
            del l[0]
            return

        root = TreeNode(int(l[0]))
        del l[0]
        root.left = self.rdeserialize(l)
        root.right = self.rdeserialize(l)

        return root




    def front_search(self, tree_base):
        '前序遍历:根-左-右'
        if tree_base == None:
            self.str_ser+="None,"
            return
        self.str_ser+=str(tree_base.val)+','
        # print(tree_base.val)
        self.front_search(tree_base.left)
        self.front_search(tree_base.right)

class Solution:
    def __init__(self):
        self.res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root==None:
            return 0
        self.front_search(root,sum)
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)

        return self.res


    def front_search(self, tree_base,sum):
        if tree_base==None:
            return
        sum-=tree_base.val
        if sum==0:
            self.res+=1
            return
        self.front_search(tree_base.left,sum)
        self.front_search(tree_base.right,sum)






if __name__ == '__main__':
    root_str = "10,5,3,3,None,None,-2,None,None,2,None,1,None,None,-3,None,11,None,None,"
    C =Codec()
    root = C.deserialize(root_str)

    S =Solution()
    print(S.pathSum(root,8))