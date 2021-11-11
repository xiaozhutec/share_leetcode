# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def reverseString(self, s):
        size = len(s)
        left, right = 0, size-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["H"]))
