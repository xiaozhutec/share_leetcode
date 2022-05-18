# -*- coding:utf-8 -*-
# !/usr/bin/env python

def get_next(m, size_m):
    """
    next 数组存放的是：截止到某一个字符，前缀子串 和 后缀子串的共有子串的「长度」
    :param m: 模式串
    :param size_m: 模式串长度
    :return:
    """
    # return [-1, 0, 0, 0, 1, 2, 0]
    # ABCDABD

    # 初始化第 1 位，由于第一位不存在前后缀子串，因此，默认设为 -1
    # 初始化第 2 位，比较前 2 位，看前缀子串 和 后缀子串的共有子串的「长度」
    next = [-1 for _ in range(size_m)]
    if m[0] == m[1]:
        next[1] = 1
    else:
        next[1] = 0
    # 计算 next 其他数值
    for i in range(2, size_m):
        if m[i] == m[next[i-1]]:
            next[i] = next[i-1]+1
        else:
            next[i] = 0
    print(next)
    return next



def kmp(n, size_n, m, size_m):
    next = get_next(m, size_m)
    i, j = 0, 0
    while i < size_n - size_m:
        while j < size_m and n[i+j] == m[j]:    # 定位到不相等的字符位置
            j += 1
        # 完全匹配
        if j == size_m:
            return i
        # 未匹配
        if j == 0:  # 如果是字符串的第一个位置，那么直接移动
            i += 1
        else:
            i += j - next[j-1]  # 移动位数=匹配的字符数-next数组匹配值（j是不匹配位，j-1就是匹配的位置）
            j = next[j-1]  # 寻找下一次比较 j 的位置，因为前缀子串是一致的
    return -1

if __name__ == '__main__':
    n = "BBC ABCDAB ABCDABCDABDE"
    m = "ABCDABD"
    # n = "GTTATAGCTGATCGCGGCGTAGCGGCGAA"
    # m = "GTAGCGGCG"
    size_n = len(n)
    size_m = len(m)
    get_next(m, size_m)
    print("res:", kmp(n, size_n, m, size_m))