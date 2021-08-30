# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def maxProfit(self, prices):
        """
        使用动态规划解决: 最多完成 2 次交易
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size == 0:
            return 0
        dp = [[0 for _ in range(size)] for _ in range(3)]
        print(dp)

        for i in range(1, 3):
            # 每一次交易的最大利润
            max_profit = -prices[0]
            for j in range(1, size):
                dp[i][j] = max(dp[i][j-1], max_profit + prices[j])
                max_profit = max(max_profit, dp[i-1][j] - prices[j])
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))
