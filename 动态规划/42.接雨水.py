# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def trap(self, height):
        """
        输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
        输出：6
        解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
                +
           +...++.+
         +.++.++++++
        left_max_height=max(height[i-1], left_max_height[i-1])
        left_max_height=[0,0,1,1,2,2,2,2,2,3,3,3]
        right_max_height=max(height[i+1], right_max_height[i+1])
        right_max_height=[3,3,3,3,3,3,3,3,2,2,1,0]
        最大单位水量=左右取最小值-本身的高度
        water=min(left_max_height[i], right_max_height[i])-height[i])
        max_water=water>=0?water:0
        max_water=[0,0,1,0,1,2,1,0,0,1,0,0]
        """
        size = len(height)
        # 小于等于 2 的时候，是接不住雨水的
        if size <= 2:
            return 0
        # 左边相对于当前位置的最大高度
        left_max_height = [0 for _ in range(size)]
        # 右边相对于当前位置的最大高度
        right_max_height = [0 for _ in range(size)]
        # 当前位置接雨水最大高度
        max_water = [0 for _ in range(size)]

        # 初始化 left_max_height, 第 0 个位置初始化为 0
        for i in range(1, size):
            left_max_height[i] = max(height[i-1], left_max_height[i-1])

        # 初始化 right_max_height, 第 size-1 个位置初始化为 0
        for j in range(1, size):
            right_max_height[size-j-1] = max(height[size-j], right_max_height[size-j])

        # 最大水量
        for k in range(1, size):
            max_water[k] = (min(left_max_height[k], right_max_height[k])-height[k] if min(left_max_height[k], right_max_height[k])-height[k]>=0 else 0)

        # 累计求单位水量
        waters = 0
        for z in range(1, size):
            waters += max_water[z]
        return waters


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))