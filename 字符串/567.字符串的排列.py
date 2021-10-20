# -*- coding:utf-8 -*-
# !/usr/bin/env python
import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        size1 = len(s1)
        size2 = len(s2)
        if size1 > size2:
            return False

        dict_s1 = collections.Counter(s1)
        dict_s2 = collections.Counter(s2[:size1-1])
        left = 0
        for right in range(size1-1, size2):
            # 增加新添加的元素
            dict_s2[s2[right]] += 1
            # 判断如果字典相同，则返回 True
            if dict_s1 == dict_s2:
                return True
            # 删除左边剔除的元素(首先需要将左边元素的 value 值减 1)
            dict_s2[s2[left]] -= 1
            # value 值为 0 的时候，就可以删除该元素了
            if dict_s2[s2[left]] == 0:
                del(dict_s2[s2[left]])
            # 窗口整体向右移动一格
            left += 1
            right += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
