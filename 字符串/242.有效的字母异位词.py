# -*- coding:utf-8 -*-
# !/usr/bin/env python
import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        字典做词频统计即可
        这里直接使用 API
        """
        dict_s1 = collections.Counter(s)
        dict_s2 = collections.Counter(t)
        print(dict_s2)
        return dict_s1 == dict_s2

    def isAnagram1(self, s, t):
        """
        自己构造 dict 对象进行比较
        collections.defaultdict() 说明文档：https://www.johngo689.com/2258/
        """
        dict_s1 = collections.defaultdict(int)
        dict_s2 = collections.defaultdict(int)
        for item1 in s:
            dict_s1[item1] += 1
        for item2 in t:
            dict_s2[item2] += 1
        return dict_s1 == dict_s2

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram1("aa", "a"))

