
## 使用递归
## 分解子问题
## 左括号进入递归，右括号退出递归，同时要返回字符串的索引




def dfs(s, i):
    res = ""
    num = 0
    while True:
        if i >= len(s):
            break
        if s[i] in "0123456789":
            num = num*10 + int(s[i])
        elif s[i] == "[":
            i, tmp = dfs(s, i+1)
            res = res + num*tmp
            num = 0
        elif s[i] == "]":
            return i, res
        elif s[i].isalpha():
            res = res + s[i]
        i = i + 1
    return res
class Solution:
    def decodeString(self, s: str) -> str:
        return dfs(s, 0)


if __name__ == "__main__":
    sl = Solution()
    print(sl.decodeString("3[a]2[bc]"))