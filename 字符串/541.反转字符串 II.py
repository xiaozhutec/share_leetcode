# -*- coding:utf-8 -*-
# !/usr/bin/env python


class Solution(object):
    def reverseStr(self, s, k):
        list_s = list(s)
        size = len(list_s)
        for index in range(0, size, 2*k):
            left = index
            right = index+k-1 if index+k < size else size-1
            while left < right:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1

        return "".join(list_s)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 2))