class MinStack_laji:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_num = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x<self.min_num:
            self.min_num = x

    def pop(self) -> None:
        self.stack.pop()



    def top(self) -> int:
        return self.stack.pop()


    def getMin(self) -> int:
        return int(self.min_num)


class MinStack:

    # 辅助栈和数据栈同步
    # 思路简单不容易出错

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]

