# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def fib(self, n):
        """
        递归处理
        :param n:
        :return:
        """
        print('计算 F(%d)' % n)
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)

    def fib_dp(self, n):
        """
        动态规划思想处理
        :param n:
        :return:
        """
        if n == 0:
            return 0
        # 1.动态数组
        dp = [0 for _ in range(n+1)]
        # 2.初始化
        dp[0] = 0
        dp[1] = 1
        # 3.动态转移方程
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def fib_dp_opt(self, n):
        """
        优化方案：空间上的优化，不使用动态数组，仅仅使用两个变量就可
        :param n:
        :return:
        """
        if n == 0:
            return 0
        # 1.2. 动态数组(空间上的优化，仅使用两个变量就可)，赋值为 0 和 1
        dp0, dp1 = 0, 1
        for i in range(2, n+1):
            dp0 = dp0 + dp1
            dp0, dp1 = dp1, dp0
        return dp1


if __name__ == '__main__':
    s = Solution()
    print(s.fib(4))
    print(s.fib_dp(4))
    print(s.fib_dp_opt(4))