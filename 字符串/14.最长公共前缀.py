# -*- coding:utf-8 -*-
# !/usr/bin/env python

"""
思路：
    方法一：Python 技巧
    方法二：纵向比较
    方法三：横向比较
    方法四：分治思想
    方法五：二分思想
"""


class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        利用 Python 本身的特性来解决
        如果每个字符串的第 i 个位置相同，那么，就该位置的字符纳入到结果集中
        以 strs = ["flower", "flow", "flight"] 为例
        将 strs 通过 zip，变换为 [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        然后相当于对 strs 纵向扫描，通过 set() 方法去重，只要大于 1 的，那么不是公共前缀的第一位
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
        和方法一类似
        需要纵向一个一个进行比较。
        在每一个纵向中，如果遇到不同的字符，则记录最长公共前缀
        """
        s = strs[0]
        size = len(s)
        lcp = 0
        tag = False
        for index in range(size):
            for item in range(len(strs)):
                # 需要判断位置 index 在 strs 中字符串是否越界
                if index < len(strs[item]) and s[index] == strs[item][index]:
                    tag = True
                else:
                    # 当匹配不到的时候，退出该次循环
                    tag = False
                    break
            if tag is True:
                lcp += 1
            else:
                break
        return s[:lcp]


    def longestCommonPrefix3(self, strs):
        """
        横向扫描
        与每一个单词进行比较
        以 ["flower", "flow", "flight"] 为例：
        将位置 0 的单词作为哨兵 s="flower" 分别于后面的几个做比较，更新公共前缀
        "flower"
        "flow"      --> 更新 s="flow"
        "flow"
        "flight"    --> 更新 s="fl"
        """
        s = strs[0]
        for index in range(1, len(strs)):
            w_index, size = 0, min(len(s), len(strs[index]))
            for w_index in range(size):
                if s[w_index] != strs[index][w_index]:
                    break
                w_index += 1
            s = s[0: w_index]
        return s

    def longestCommonPrefix4(self, strs):
        """
        分治求解
        ["flower", "flow", "flight", "flink"]
        -> ["flower", "flow"] ["flight", "flink"]
        -> ["flow"] ["fli"]
        -> ["fl"]
        """
        def lcp(left, right):
            if left == right:
                return strs[left]
            mid = (left + right)//2
            # 得到左右两个字符串
            left_str, right_str = lcp(left, mid), lcp(mid+1, right)
            index, min_len = 0, min(len(left_str), len(right_str))
            while index < min_len:
                if left_str[index] != right_str[index]:
                    return left_str[:index]
                index += 1
            return left_str[:index]
        return lcp(0, len(strs)-1)


    def longestCommonPrefix5(self, strs):
        """
        二分查找
        ["flower", "flow", "flight", "flink"]
        "flower" -> left=0,right=5,mid=(left+right)//2=2 => 左:["flo"], 右:["wer"]
        如果左:["flo"]在后面每个单词[left:mid]中，则 left=mid+1, mid=(left+right)//2
        否则，right=mid, mid=(left+right)//2

        所以，right=2，mid=1，左:["fl"]，右:["o"]
        如果左:["fl"]在后面每个单词[left:mid]中，则 left=mid+1,mid=(left+right)//2
        否则，right=mid, mid=(left+right)//2
        """
        s = strs[0]
        lcp = ""
        left, right = 0, len(strs[0])-1
        mid = (left+right)//2
        # 只有一个字符串的情况下
        if len(strs) == 1:
            return s
        while left <= right:
            tag = True
            # 轮询判断子串与后面每个字符串对应位置的子串是否相同
            for i in range(1, len(strs)):
                if s[left:mid+1] not in strs[i][left:mid+1]:
                    tag = False
                    break

            # 左边子串存在后面每个字符串中
            if tag is True:
                # 将匹配到的子串加入到结果集中
                lcp += s[left:mid+1]
                left = mid+1
                mid = (left+right)//2
            # 左边子串不存在后面每个字符串中
            else:
                if right == mid: # 当 right == mid，说明right指针已经无法靠左移动了，退出循环
                    break
                else:
                    right = mid
                mid = (left+right)//2
        return lcp


if __name__ == '__main__':
    s = Solution()
    # print(s.longestCommonPrefix1(["flower", "flow", "flight"]))
    # print(s.longestCommonPrefix3(["flower", "flow", "flight", "flink"]))
    print(s.longestCommonPrefix5(["flower", "flow", "flownlp", "flowcv"]))
    # print(s.longestCommonPrefix5(["flower", "flower", "flower", "flower"]))
    # print(s.longestCommonPrefix5(["a", "b"]))
