

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = list()
        stack.append(-1)
        max_len = 0
        length = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    if stack:
                        length = i - stack[-1]
            max_len = length if length > max_len else max_len
        return max_len
    
if __name__ == "__main__":
    sl = Solution()
    print(sl.longestValidParentheses(")()())"))