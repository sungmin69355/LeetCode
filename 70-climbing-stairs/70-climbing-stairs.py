class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for i in range(n)]
        for i in range(1, n):
            if i <= 2:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-2] + dp[i-1]
        return dp[n-1]