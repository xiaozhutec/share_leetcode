# -*- coding:utf-8 -*-
# !/usr/bin/env python

"""
BBC ABCDAB ABCDABCDABDE
ABCDABD
"""


def get_str_hash(n, n_size):
    """
    获取字符串不同子串长度为「模式串」长度的哈希值
    :param n:
    :param n_size:
    :return:
    """
    pass



def RK(n, size_n, m, size_m):
    """
    利用哈希值进行比较，实现时间复杂度为 O(N) 的计算
    :param n:
    :param size_n:
    :param m:
    :param size_m:
    :return:
    """
    pass




if __name__ == '__main__':
    n = "BBC ABCDAB ABCDABCDABDE"
    m = "ABCDABD"
    # n = "GTTATAGCTGATCGCGGCGTAGCGGCGAA"
    # m = "GTAGCGGCG"
    size_n = len(n)
    size_m = len(m)
    print(BF(n, size_n, m, size_m))
    print(RK(n, size_n, m, size_m))