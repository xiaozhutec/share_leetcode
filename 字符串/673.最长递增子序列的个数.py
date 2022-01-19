# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    """
    1 定义状态
        dp[i]：到 nums[i] 为止的最长递增子序列长度
        count[i]：到 nums[i] 为止的最长递增子序列个数
        ps：是截止到位置 i 为止，要包含位置i的元素，而不是符合<=i之前字符串或者整体最长递增子序列
    2 初始化状态
        dp = [1] * n：代表最长递增子序列的长度至少为1
        count = [1] * n：代表最长递增子序列的个数至少为1
    3 状态转移
        对于每一个数nums[i]，看在它之前的数nums[j](0<=j<i)是否比当前数nums[i]小
            如果 nums[i]>nums[j]，那么相当于到nums[j]为止的最长递增子序列长度到nums[i]增加了1，到nums[i]为止的最长递增子序列长度就变成了 dp[i]=dp[j]+1；
            但是因为满足 nums[i]>nums[j] 的 nums[j] 不止一个，dp[i] 应该取这些 dp[j]+1 的最大值，并且这些 dp[j]+1 还会有相等的情况，一旦相等，到 nums[i] 为止的最长递增子序列个数就应该增加了。
            因此，具体的状态转移如下，在 nums[i]>nums[j] 的大前提下：
        3.1 如果 dp[j]+1>dp[i]，说明最长递增子序列的长度增加了，dp[i]=dp[j]+1，长度增加，数量不变 count[i]=count[j]
        3.2 如果 dp[j]+1==dp[i]，说明最长递增子序列的长度并没有增加，但是出现了长度一样的情况，数量增加 count[i]+=count[j]
    4 记录最长递增子序列的最大长度 max_length
    5 遍历dp数组，如果dp数组记录的最大长度dp[i]等于max_length，将对应的数量count[i]加到结果res中
    """
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
                        dp[i] = dp[j] + 1
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
    print(s.findNumberOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3]))
    print("=====================")
    print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
