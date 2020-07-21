# Definition for a binary tree node.
class TreeNode(object):
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





if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    S = Codec()
    str = S.serialize(root)
    a = S.deserialize(str)
    print(a.val)
