# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):

    def findNumberOfLIS(self, nums):
        size = len(nums)
        if size == 1:
            return 1
        # 最长递增子序列长度
        max_len = 1
        # 初始化dp和count数组，初始化为全 1
        dp = [1 for _ in range(size)]
        count = [1 for _ in range(size)]

        for i in range(1, size):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = max(dp[i], dp[j]+1)
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
                # 记录最长子序列长度
                if max_len < dp[i]:
                    max_len = dp[i]
        # 获取最长子序列个数
        max_len_num = 0
        for i in range(size):
            if dp[i] == max_len:
                max_len_num += count[i]
        return max_len_num


if __name__ == '__main__':
    s = Solution()
    # print(s.findNumberOfLIS([1, 3, 2, 6, 7, 9, 4, 10, 5, 6]))
    # print(s.findNumberOfLIS([1, 3, 6, 7, 9, 4, 11, 10, 5, 6]))
    # print(s.findNumberOfLIS([1, 1, 1]))
    # print(s.findNumberOfLIS([2, 2, 2, 2, 2]))
    print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
    # print(s.findNumberOfLIS([2, 1]))
    # print(s.findNumberOfLIS([1, 2]))
#     1, 3, 5, 4, 7
# dp  1  2  3
# co  1  1  1
#
# dp 更新的条件是nums各个位置的值
# count 更新的条件是，如果 dp 值增加了，说明长度增加，所以个数不加；如果dp值不变，说明长度未增加，个数要增加
#
# [1, 3, 5, 4, 7]
# [1, 2, 3, 3, 4]
# [1, 1, 1, 1, 2]