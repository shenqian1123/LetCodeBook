

## 使用一个赋值栈来记录过往最小值



class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        else:
            return None


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None


    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None




if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    val = 3
    obj.push(7)
    obj.push(6)
    obj.push(4)
    obj.push(3)
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
