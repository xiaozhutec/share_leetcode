# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def climbStairs(self, n):
        """
        爬楼梯
        1.定义动态数组 dp
        2.动态转移方程；dp[i] = dp[i-2] + dp[i-1]
        3.初始化：dp[1]=1, dp[2]=2
        """
        if n == 1:
            return 1
        dp = [ 1 for _ in range(n+1)]
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]

    def climbStairs_opt(self, n):
        """
        空间方面优化：dp[i]的状态至于前两个状态有关
        因此，可以定义两个单独的变量即可！
        """
        if n == 1:
            return 1
        dp1, dp2 = 1, 2
        for i in range(3, n+1):
            dp1 = dp1 + dp2
            dp1, dp2 = dp2, dp1

        return dp2


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs_opt(3))
