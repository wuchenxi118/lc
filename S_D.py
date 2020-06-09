
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.Dindex = 0

    def Serialize(self, root):
        # write code here
        if root == None:
            return ""
        res = ""
        stack = []
        p = root
        while (p != None or len(stack) != 0):
            if p != None:
                res += str(p.val)
                res += '!'
                stack.append(p)
                p = p.left
            else:
                res += '#'
                res += '!'
                p = stack[-1].right
                del stack[-1]
        return res

    def Deserialize(self, s):
        # write code here
        if not s:
            return None
        Node_list = s.split('!')[:-1]
        return self.helpDeserialize(Node_list)

    def helpDeserialize(self,strs):
        print(self.Dindex)
        if strs[self.Dindex] == "#":
            self.Dindex += 1
            return

        root = TreeNode(strs[self.Dindex])
        self.Dindex += 1

        root.left = self.helpDeserialize(strs)
        root.right = self.helpDeserialize(strs)
        if self.Dindex > len(strs)-1:
            return root
        return root



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

a.left = b
a.right = c
b.left = d

S = Solution()
ss = S.Serialize(a)
print(ss)
x = S.Deserialize(ss)
print(x)
