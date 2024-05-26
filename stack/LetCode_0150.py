from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for elem in tokens:
            if elem in ["+", "-", "*", "/"]:
                right = int(stack.pop())
                left = int(stack.pop())
                if elem == "/":
                    stack.append(str(int((left) / (right))))
                elif elem == "+":
                    stack.append(str(left + right))
                elif elem == "*":
                    stack.append(str(left * right))
                else:
                    stack.append(str(left - right))

            else:
                stack.append(elem)
        return int(stack.pop())

if __name__ == "__main__":
    sl = Solution()
    print(sl.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(sl.evalRPN(tokens=["2","1","+","3","*"]))