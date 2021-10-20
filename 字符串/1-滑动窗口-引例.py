# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):

    def sumSlidingWindow(self, s, w):
        """
        计算窗口内数字之和
        :param s: 主字符串
        :param w: 窗口大小
        :return: 返回每个窗口数字和
        """
        sum = 0
        res = []
        # 计算第一个窗口数字之和
        for item in range(5):
            sum += s[item]
        res.append(sum)
        # 后面利用滑动窗口思想进行计算
        for item in range(w, len(s)):
            sum -= s[item-w]
            sum += s[item]
            res.append(sum)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.sumSlidingWindow([5, 1, 8, 9, 6, 2, 3, 1, 9, 6], 5))
