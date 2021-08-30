# -*- coding:utf-8 -*-
# !/usr/bin/env python


class Solution(object):

    def maxProfit(self, prices):
        size = len(prices)
        if size == 0 or size == 1:
            return 0
        # 定义动态数组
        dp = [[0 for _ in range(size)] for _ in range(2)]
        # 初始化动态数组
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        # 动态方程
        for j in range(1, size):
            dp[0][j] = max(dp[0][j - 1], dp[1][j - 1] + prices[j])
            dp[1][j] = max(dp[1][j - 1], -prices[j])
        return dp[0][-1]

    def maxProfit_opt(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size == 0 or size == 1:
            return 0
        dp1 = 0
        dp2 = -prices[0]
        for j in range(1, size):
            tmp1 = max(dp1, dp2+prices[j])
            tmp2 = max(dp2, -prices[j])
            dp1, dp2 = tmp1, tmp2
        return dp1

    def maxProfit_opt1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size == 0 or size == 1:
            return 0
        _max = 0
        min_price = prices[0]
        for i in range(1, size):
            min_price = min(min_price, prices[i])
            _max = max(_max, prices[i] - min_price)
        return _max


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit_opt([7, 1, 5, 3, 6, 4]))
