
## 使用栈
## cond1:遍历字符串，如果不是右括号，那么就直接往栈里面放元素
## cond2:如果是右括号，那么开始弹出元素，直到弹出的当前元素为数字且测试栈顶为空或者栈顶不为数字时结束
## 将cond2过程依次弹出的元素逆序拼接，并提取出数字和字符串，进行字符串扩展，同时将扩展后的字符串重新放入栈中
## 字符串遍历完成，将栈中的元素依次弹出，并逆序拼接

class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        sub = ""
        result = ""
        for elem in s:
            if elem != "]":
                stack.append(elem)
            else:
                while True:
                    top = stack.pop()
                    sub = top + sub
                    if top in "0123456789":
                        if (stack and stack[-1] not in "0123456789") or (not stack):
                            temp = int(sub.split("[")[0])*sub.split("[")[1]
                            stack.append(temp)
                            sub = ""
                            break
        result = ""
        while True:
            if not stack:
                break
            val = stack.pop()
            result = val + result

        return result
                    

if __name__ == "__main__":
    sl = Solution()
    sl.decodeString("3[a]2[bc]")