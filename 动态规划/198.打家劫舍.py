# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def rob(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        # 1. 动态数组
        dp = [0 for _ in range(size+1)]
        # 2. 初始化
        dp[0] = 0
        # 3. 动态方程
        #   偷：dp[i] = nums[i-1] + dp[i-2]
        #   不偷：dp[i] = dp[i-1]
        for i in range(1, size+1):
            dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]))
