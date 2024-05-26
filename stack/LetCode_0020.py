class Solution:
    ## 左括号入左栈
    ## 右括号出栈比较

    def isValid(self, s: str) -> bool:
        left_stack = list()
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                left_stack.append(s[i])
            else:
                if len(left_stack) != 0:
                    if (left_stack.pop() + s[i] not in ["()", "[]", "{}"]):
                        return False
                else:
                    return False
        return True if len(left_stack) == 0 else False
            
            
if __name__ == "__main__":
    sl = Solution()
    print(sl.isValid("([)]"))