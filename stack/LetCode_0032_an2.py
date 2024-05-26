
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = len(s)*[0]
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                elif s[i - 1] == ")" and s[i - dp[i-1] - 1] == "(" and i - dp[i-1] - 1 >= 0:
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] + 2 if i - dp[i - 1] >= 2 else 2)
            maxans = max(maxans, dp[i])
        return maxans

    
if __name__ == "__main__":
    sl = Solution()
    print(sl.longestValidParentheses(")()())"))