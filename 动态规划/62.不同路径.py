# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def uniquePaths(self, m, n):
        # 动态数组的定义，以及初始化首行和首列都为 1
        # 初始化首行和首列都为 1 的原因：按照首行一直移动，路径是能我 1，首列同理。
        dp = [[1 for _ in range(m)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths_opt(self, m, n):
        if m < n:
            m, n = n, m
        dp = [1 for _ in range(m)]

        for i in range(1, n):
            for j in range(1, m):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]




if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))
    print(s.uniquePaths_opt(7, 3))
