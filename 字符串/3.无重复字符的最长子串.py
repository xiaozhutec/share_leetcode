# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        :solution: 滑动窗口解决
        a b c a b c b b
        0 1 2 3 4 5 6 7
        words = {元素: 对应的下标}
        发现 words 集合中已经包含了 right 位置的元素时，将 left 指向重复元素的下一个元素，同时 right++
        如果s=0，之间返回0
        length = max(right-left+1, length)
        left, right = 0, 0
        len = 1

        ① left=0，right=0，s[right]在words中未发现重复值，length=max(1,1)=1，s[right]写入words={'a':0}
        ② left=0，right=1，s[right]在words中未发现重复值，length=max(2,1)=2，s[right]写入words={'a':0,'b':1}
        ③ left=0，right=2，s[right]在words中未发现重复值，length=max(3,2)=3，s[right]写入words={'a':0,'b':1,'c':2}
        ④ left=0，right=3，s[right]在words中发现重复值，words['a']=0，故 left=0+1=1，words更新 a 的值为{'a':3,'b':1,'c':2}，length=max(3,3)=3
        ⑤ left=1，right=4，s[right]在words中发现重复值，words['b']=1，故 left=1+1=2，words更新 b 的值为{'a':3,'b':4,'c':2}，length=max(3,3)=3
        ⑥ left=2，right=5，s[right]在words中发现重复值，words['c']=2，故 left=2+1=3，words更新 c 的值为{'a':3,'b':4,'c':5}，length=max(3,3)=3
        ⑦ left=3，right=6，s[right]在words中发现重复值，words['b']=4，故 left=4+1=5，words更新 b 的值为{'a':3,'b':6,'c':5}，length=max(2,3)=3
        ⑧ left=5，right=7，s[right]在words中发现重复值，words['b']=6，故 left=6+1=7，words更新 b 的值为{'a':3,'b':7,'c':5}，length=max(1,3)=3
        得到最终的答案：length=3
        """
        if not s:
            return 0
        left, right = 0, 0
        length = 1
        words = {}
        for right, v in enumerate(s):
            if s[right] in words.keys():
                # 中间有可能left已经更新到后边，而新判断的元素可能在前面，会导致left变小，所以需要采用max来进行判断
                # 举例：abba，执行到第二个b的时候，left=2，此时words={'a':0,'b':2}。后面再判断最后的a的时候，就会使得left=0+1=1
                # 因此，需要max(words.get(v) + 1, left)
                print(words.get(v) + 1, left)
                left = max(words.get(v) + 1, left)
            length = max(right-left+1, length)
            # 将当前值的 value 值覆盖
            words[v] = right
        print(words)
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abba"))
    # print(s.lengthOfLongestSubstring("abcabcbb"))
