# -*- coding:utf-8 -*-
# !/usr/bin/env python
import collections

class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t) or not s:
            return ""
        left, right = 0, 0
        # 初始化最小覆盖子串长度，为 s 的长度
        win_len = len(s)
        # 最小覆盖子串
        win_str = ""
        len_t = len(t)
        distance = 0
        win_dict = collections.Counter()
        t_dict = collections.Counter(t)

        while right < len(s):
            print("again...")
            if win_dict[s[right]] < t_dict[s[right]]:
                distance += 1
            win_dict[s[right]] += 1
            right += 1

            while distance == len_t:
                print("覆盖时：", s[left: right+1])
                if win_dict[s[left]] > t_dict[s[left]]:
                    win_dict[s[left]] -= 1
                    left += 1
                    print("覆盖后：", s[left: right + 1])
                else:
                    if right-left+1 < win_len:
                        win_len = right-left+1
                        win_str = s[left: right+1]
                    break
        return win_str


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECOCEBACC", "ABCC"))