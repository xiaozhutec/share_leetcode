# -*- coding:utf-8 -*-
# !/usr/bin/env python

"""
BBC ABCDAB ABCDABCDABDE
ABCDABD
"""


def BF(n, size_n, m, size_m):
    for i in range(size_n-size_m):
        j = 0
        while j < size_m and n[i+j] == m[j]:
            j += 1
        if j == size_m:
            return i
        i += 1
    return -1


if __name__ == '__main__':
    n = "BBC ABCDAB ABCDABCDABDE"
    m = "ABCDABD"
    # n = "GTTATAGCTGATCGCGGCGTAGCGGCGAA"
    # m = "GTAGCGGCG"
    size_n = len(n)
    size_m = len(m)
    print(BF(n, size_n, m, size_m))
