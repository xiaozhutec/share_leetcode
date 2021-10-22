# -*- coding:utf-8 -*-
# !/usr/bin/env python
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        字典做词频统计即可
        在每一步骤执行的时候，进行和 p 对应的字典进行比较
        """
        size_s = len(s)
        size_p = len(p)
        dict_s = collections.Counter(s[0:size_p-1])
        dict_p = collections.Counter(p)
        res = []

        for i in range(size_p-1, size_s):
            dict_s[s[i]] += 1
            if i >= size_p:
                dict_s[s[i-size_p]] -= 1
                if dict_s[s[i-size_p]] == 0:
                    del(dict_s[s[i-size_p]])
            if dict_s == dict_p:
                res.append(i-size_p+1)
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("abab", "ab"))

# "cbaebabacd", "abc"
# "abab", "ab"