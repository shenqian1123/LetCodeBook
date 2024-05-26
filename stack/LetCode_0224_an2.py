
## 迭代解法，使用stack

class Solution:
    def calculate(self, s: str) -> int:
        stack = list()
        for str_ in s:
            if str_ != ")":
                stack.append(str_)
            else:
                exp = []
                while True:
                    val = stack.pop()
                    if val == "(":
                        break
                    exp.insert(0, val)
                stack.append(str(self.add(exp)))
        exp = []
        while True:
            if len(stack) == 0:
                break
            val = stack.pop()
            exp.insert(0, val)
        return int(self.add(exp))
            


    @staticmethod
    def add(s):
        i = 0
        res = 0
        num = "0"
        token = ""
        while True:
            if i >= len(s):
                break
            if s[i] == " ":
                pass
            elif s[i] in "+-":
                token = s[i]
            elif s[i] in "0123456789":
                while True:
                    num = num + s[i]
                    if i == len(s) - 1 or s[i] in "0123456789" and s[i+1] not in "0123456789":
                        break
                    i = i + 1
                if token:
                    if token == "-":
                        res = res - int(num)
                    else:
                        res = res + int(num)
                    num = "0"
                    token = ""
                else:
                    res = int(num)
                    num = "0"
            elif len(s[i]) >= 2:
                num = s[i]
                if token:
                    if token == "-":
                        res = res - int(num)
                    else:
                        res = res + int(num)
                    num = "0"
                    token = ""
                else:
                    res = int(num)
                    num = "0"
            i = i + 1
        return res

            

if __name__ == "__main__":
    sl = Solution()
    # print(sl.add(" 2-1 + 2 "))
    print(sl.calculate("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"))