# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def lengthOfLIS(self, nums):
        size = len(nums)
        if size == 1:
            return 1
        # 1.初始化dp数组，内容初始化为全1
        dp = [1 for _ in range(size)]
        # 2.动态方程定义：dp[i] = max(dp[i], dp[j]+1), 0<=j<=i-1 and nums[i]>nums[j]
        for i in range(1, size):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))

# [1, 3, 6, 7, 9, 4, 10, 5, 6]
# [1, 2, 3, 4, 5, 3, 6,  4, 5]













