# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def longestPalindrome(self, s):
        """
        思路：最长回文子串，用到动态规划的理由是，在不断判断过程中，如果两端字符相同，而且两端字符里面是回文串，那么现在判断的子串就是回文串
        基于这个思路，我们进行如下求解：
        定义 dp[i][j] 表示字符串 s 从 i 到 j 是否是回文串。
        状态转移方程为 dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]，解释：
        1. 首先必须要判断 dp[i]==dp[j] 是否成立，否则即使内部是回文串，也不会成立
        2. 判断位置 i 和 j 的相邻内部 dp[i+1][j-1]，是否为回文串
        以上两点同时成立，dp[i][j]是回文串才成立。
          a b c b d
        a T F F F F
        b   T F T F
        c     T F F
        b       T F
        d         T
        :param s: 字符串
        :return: 最长回文子串
        """
        size = len(s)
        if size == 1:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True

        max_len = 1     # 记录回文串长度
        start = 0       # 记录回文串起始位置
        for j in range(1, size):
            for i in range(0, j):
                dp[i][j] = (s[i] == s[j]) and (j - i <=2 or dp[i + 1][j - 1])
                if dp[i][j]:
                    if j-i+1 > max_len:
                        max_len = j - i + 1
                        start = i

        return s[start: start+max_len]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abcbd"))
