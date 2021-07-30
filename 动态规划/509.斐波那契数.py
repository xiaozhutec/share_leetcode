# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def tribonacci(self, n):
        """
        递归处理
        :param n:
        :return:
        """
        print('计算 F(%d)' % n)
        if n < 2:
            return n
        return self.tribonacci(n-1) + self.tribonacci(n-2)

    def tribonacci_dp(self, n):
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



if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(4))
    print(s.tribonacci_dp(4))