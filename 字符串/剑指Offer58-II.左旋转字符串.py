# -*- coding:utf-8 -*-
# !/usr/bin/env python


class Solution(object):
    # 1. 拼接起来，直接截取
    def reverseLeftWords(self, s, n):
        size = len(s)
        s2 = s + s
        return s2[n:size+n]

    # 2. 循环放置到最后，然后截取
    def reverseLeftWords1(self, s, n):
        size = len(s)
        for i in range(n):
            s += s[i]
        return s[n:]


if __name__ == '__main__':
    s = Solution()
    print(s.reverseLeftWords("abcdefg", 2))
    print(s.reverseLeftWords1("abcdefg", 2))
