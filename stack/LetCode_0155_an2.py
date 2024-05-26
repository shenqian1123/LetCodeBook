

## 不适用额外空间
## 使用栈保存差值



class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_value = None


    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_value = val
        else:
            diff = val - self.min_value
            self.stack.append(diff)
            self.min_value = self.min_value if diff >= 0 else val


    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val >= 0:
                val = val + self.min_value
            else:
                val, self.min_value = self.min_value, self.min_value - val
            return val
        else:
            return None


    def top(self) -> int:
        if self.stack:
            val = self.stack[-1]
            if val >= 0:
                val = val + self.min_value
            else:
                val = self.min_value
            return val
        else:
            return None


    def getMin(self) -> int:
        if self.stack:
            return self.min_value
        else:
            return None





if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    val = 3
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
