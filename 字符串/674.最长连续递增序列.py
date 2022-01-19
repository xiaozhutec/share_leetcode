# -*- coding:utf-8 -*-
# !/usr/bin/env python


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        既然是连续递增，很容易想到贪心策略来解决
        初始化 start=0，然后移动 i 到后面每个位置
        如果 nums[i]>nums[i-1]，则 i++
        如果 nums[i]<=nums[i-1]，则 start=i
        """
        size = len(nums)
        start = 0
        res_len = 0
        for i in range(size):
            if nums[i] <= nums[i-1]:
                start = i
            res_len = max(res_len, i-start+1)

        return res_len


if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1, 3, 5, 4, 7]))