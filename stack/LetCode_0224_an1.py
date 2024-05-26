
## 递归解法
## 碰到左括号，进入递归，碰到右括号，退出递归，并返回子问题的解及右括号的idex


def dfs(s, i):
    res = 0
    num = "0"
    token = ""
    while True:
        if i >= len(s):
            break
        if s[i] in "+-":
            token = s[i]
        elif s[i] in "0123456789":
            while True:
                num = num + s[i]
                if i == len(s) - 1 or (s[i] in "0123456789" and s[i+1] not in "0123456789"):
                    break
                i = i + 1
            if token:
                num = int(num)
                if token == "-":
                    res = res - num
                else:
                    res = res + num
                num = "0"
                token = ""
            else:
                num = int(num)
                res = num 
                num = "0"
        elif s[i] == "(":
            num, i = dfs(s, i + 1)
            if token:
                num = int(num)
                if token == "-":
                    res = res - num
                else:
                    res = res + num
                num = "0"
                token = ""
            else:
                num = int(num)
                res = num 
                num = "0"   
        elif s[i] == ")":
            return res, i
        elif s[i] == " ":
            pass

        i = i + 1
    return res

class Solution:
    def calculate(self, s: str) -> int:
        return dfs(s, 0)

if __name__ == "__main__":
    sl = Solution()
    print(sl.calculate(" 2-1 + 2 "))