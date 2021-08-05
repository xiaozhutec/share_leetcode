# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def rob(self, nums):
        """
        由于题目要求：1.所有的房屋围成一圈；2.相邻房屋不能同时偷
        三种情况：
        a.不偷首偷尾
        b.偷首不偷尾
        c.首尾均不偷
        显然，我们要舍弃 c 这种情况
        :param nums:
        :return:
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        def handle(num, size):
            # 1.动态数组定义
            dp = [0 for _ in range(0, size+1)]
            # 2.初始化
            dp[0] = 0
            # 3.动态方程
            # a.偷 dp[i] = num[i-1] + dp[i-2]
            # b.不偷 dp[i] = dp[i-1]
            # 最后取偷与不偷中的最大值
            for i in range(1, size+1):
                dp[i] = max(num[i-1] + dp[i-2], dp[i-1])
            return dp[-1]

        res1 = handle(nums[1:], size-1)
        res2 = handle(nums[:-1], size-1)
        return max(res1, res2)

    def rob_opt(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        def handle(num, size):
            dp1, dp2 = 0, num[0]
            for i in range(2, size+1):
                dp1 = max(dp2, nums[i - 1] + dp1)
                dp1, dp2 = dp2, dp1
            return dp2

        res1 = handle(nums[1:], size-1)
        res2 = handle(nums[:-1], size-1)
        return max(res1, res2)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1, 1]))
    print(s.rob_opt([2,3,2]))

