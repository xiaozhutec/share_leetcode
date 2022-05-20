# -*- coding:utf-8 -*-
# !/usr/bin/env python

"""
BBC ABCDAB ABCDABCDABDE
ABCDABD
"""


def get_str_hash(n, n_size, size_m, hash_code):
    """
    获取字符串不同子串长度为「模式串」长度的哈希值
    BK 算法的核心思想是：对于所有位置 i，高效计算位置 i+1 的哈希值
    即：计算位置 i+1 哈希值时，将位置 i 的哈希值减去第一个数字的值，乘以R，再加上最后一个数字的值（位置i+size_m）

    哈希函数：通过计算字符串每个字符对应的 ascii 码，计算字符串数值
    例如：
    "abc" ==> 97*10^2 + 98*10 + 99 = (97*10 + 98) * 10 + 99
    """
    hash_code_sub = 0
    pow_m = pow(256, size_m-1)
    # 先找出 size_m 长度的哈希值
    for i in range(size_m-1):
        hash_code_sub = (hash_code_sub + ord(n[i])) * 256
    hash_code_sub = hash_code_sub + ord(n[size_m - 1])  # 最后一位直接加上即可，不需要乘以 256
    print("h", hash_code_sub)
    if hash_code_sub == hash_code:
        return 0

    # 计算往后的哈希值
    for j in range(size_m, size_n):
        # - 首位
        hash_code_sub = (hash_code_sub - ord(n[j-size_m])*pow_m) * 256
        # + 末位
        hash_code_sub = hash_code_sub + ord(n[j])
        if hash_code_sub == hash_code:
            return j-size_m+1
    return -1


def RK(n, size_n, m, size_m):
    """
    利用哈希值进行比较，实现时间复杂度为 O(N) 的计算
    """
    hash_code = 0
    for i in range(size_m-1):
        hash_code = (hash_code + ord(m[i])) * 256
    hash_code = hash_code + ord(m[size_m-1])     # 最后一位直接加上即可，不需要乘以 256
    print(hash_code)    # 6447972
    return get_str_hash(n, size_n, size_m, hash_code)


if __name__ == '__main__':
    n = "BBC ABCDAB ABCDABCDABDE"
    m = "ABCDABD"
    # n = "GTTATAGCTGATCGCGGCGTAGCGGCGAA"
    # m = "GTAGCGGCG"
    # n = "acbcd"
    # m = "bcd"
    size_n = len(n)
    size_m = len(m)
    print(RK(n, size_n, m, size_m))
