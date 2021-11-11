# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def rotateString(self, s, goal):
        """
        旋转词有一个很显著的特点：字符串 s 一定是 goal+goal 的子串
        比如：字符串 "abcde" 一定是 "cdeabcdeab" 的子串
        利用上述特点进行判断
        """
        return len(s) == len(goal) and s in goal+goal


    def rotateString1(self, s, goal):
        """
        这个题目，咱们用
        主串：A B A C A B D C A B A B D C A B D A
        模式串：A B D C A B D
        下面就kmp算法进行一步一步的过程说明：
        ① 先来做一个前后缀表
        0 A  -- 前后缀为空，最长公共元素为[]，长度为 0
        0 A B  -- 前缀为[A]，后缀为[B]，最长公共元素为[]，长度为 0
        0 A B D  -- 前缀为[A, AB]，后缀为[BD, D]，最长公共元素为[]，长度为 0
        0 A B D C  -- 前缀为[A, AB, ABD]，后缀为[BDC, DC, C]，最长公共元素为[]，长度为 0
        1 A B D C A  -- 前缀为[A, AB, ABD, ABDC]，后缀为[BDCA, DCA, CA, A]，最长公共元素为[A]，长度为 1
        2 A B D C A B  -- 前缀为[A, AB, ABD, ABDC, ABDCA]，后缀为[BCCAB, CCAB, CAB, AB, B]，最长公共元素为[AB]，长度为 2
        3 A B D C A B D  -- 前缀为[A, AB, ABD, ABDC, ABDCA, ABDCAB]，后缀为[BDCABD, DCABD, CABD, ABD, BD, D]，最长公共元素为[ABD]，长度为 3

        我们得到的前后缀最长公共长度记为 next=[0 0 0 0 1 2 3]
        ② 逐步匹配
        A B A C A B D C A B A B D C A B D A
         👇
        A B D C A B D
        0 0 0 0 1 2 3
        已匹配的字符数-前后缀表对应的数字：2-0=2

        A B A C A B D C A B A B D C A B D A
           👇
            A B D C A B D
            0 0 0 0 1 2 3
        已匹配的字符数-前后缀表对应的数字：1-0=1

        A B A C A B D C A B A B D C A B D A
             👇
              A B D C A B D
              0 0 0 0 1 2 3
        已匹配的字符数-前后缀表对应的数字：0-(-1)=1（一个都没有匹配上的时候，记做-1）

        A B A C A B D C A B A B D C A B D A
                         👇
                A B D C A B D
                0 0 0 0 1 2 3
        已匹配的字符数-前后缀表对应的数字：6-2=4

        A B A C A B D C A B A B D C A B D A
                         👇
                        A B D C A B D
                        0 0 0 0 1 2 3
        已匹配的字符数-前后缀表对应的数字：2-0=2

        A B A C A B D C A B A B D C A B D A
                                       👇
                            A B D C A B D
                            0 0 0 0 1 2 3
        已匹配的字符数-前后缀表对应的数字：2-0=2

        此时完全匹配上!

        理解：
        根据前后缀可以得到公共前后缀，进而得到要移动的长度
        直接向后移动模式串，使得前缀子串匹配到后缀的位置，就能保证当前指针前的所有字符是匹配的
        """
        size_s = len(s)
        size_goal = len(goal)
        # if size != len(goal):
        #     return False
        # if size == 0:
        #     return True
        # 0 A  -- 前后缀为空，最长公共元素为[]，长度为 0
        # 0 A B  -- 前缀为[A]，后缀为[B]，最长公共元素为[]，长度为 0
        # 0 A B D  -- 前缀为[A, AB]，后缀为[BD, D]，最长公共元素为[]，长度为 0
        # 0 A B D C  -- 前缀为[A, AB, ABD]，后缀为[BDC, DC, C]，最长公共元素为[]，长度为 0
        # 1 A B D C A  -- 前缀为[A, AB, ABD, ABDC]，后缀为[BDCA, DCA, CA, A]，最长公共元素为[A]，长度为 1
        # 2 A B D C A B  -- 前缀为[A, AB, ABD, ABDC, ABDCA]，后缀为[BCCAB, CCAB, CAB, AB, B]，最长公共元素为[AB]，长度为 2
        # 3 A B D C A B D  -- 前缀为[A, AB, ABD, ABDC, ABDCA, ABDCAB]，后缀为[BDCABD, DCABD, CABD, ABD, BD, D]，最长公共元素为[ABD]，长度为 3
        # 构造 next 数组 ABDCABD
        # next = []
        # for i in range(size_s):
        #     print(i)

        nxt = [-1] * len(s)
        j = -1
        for i in range(1, len(s)):
            while (j >= 0 and s[j+1] != s[i]):
                j = nxt[j]
            if s[j+1] == s[i]:
                j += 1
            nxt[i] = j
        return nxt







if __name__ == '__main__':
    s = Solution()
    # print(s.rotateString('abcde', 'cdeab'))
    # print(s.rotateString1('abcde', 'cdeab'))
    print(s.rotateString1('ABDCABD', 'ABACABDCABABDCABDA'))

    # 1:
    # 输入: A = 'abcde', B = 'cdeab'
    # 输出: true
    #
    # 2:
    # 输入: A = 'abcde', B = 'abced'
    # 输出: false
