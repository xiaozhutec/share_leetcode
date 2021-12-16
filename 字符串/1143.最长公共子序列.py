# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        利用动态规划的思路进行求解
        dp[i][j] = dp[i-1][j-1] + 1              ;text1[i] == text2[j]
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])   ;text1[i] != text2[j]
        """
        size1 = len(text1)
        size2 = len(text2)
        # 1 先定义 dp 数组
        dp = [[0 for _ in range(size1)] for _ in range(size2)]

        # 2 初始化 dp 数组的第 0 行和第 0 列
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1, size1):
            dp[0][i] = 1 if dp[0][i-1] == 1 else int(text1[i] == text2[0])
        for j in range(1, size2):
            dp[j][0] = 1 if dp[j-1][0] == 1 else int(text2[j] == text1[0])

        # 3 动态方程进行求解
        for i in range(1, size2):
            for j in range(1, size1):
                if text2[i] == text1[j]:
                    # 注意这里是dp[i-1][j-1]+1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("abcde", "ace"))