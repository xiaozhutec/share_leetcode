# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        solution 1: 利用 Python 本身的特性来解决
        如果每个字符串的第 i 个位置相同，那么，就该位置的字符纳入到结果集中
        """
        lcp = ""
        for tmp in zip(*strs):
            if len(set(tmp)) == 1:
                lcp += tmp[0]
            else:
                break
        return lcp

    def longestCommonPrefix2(self, strs):
        """
        取第一个单词，和后面每个单词做比较，直到最后一个单词
        整个过程存储相同前缀的子串
        """
        size = len(strs)
        if size == 0 or size == 1:
            return s


class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.longestCommonPrefix1(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix2(["a", "a", "b"]))