# -*- coding:utf-8 -*-
# !/usr/bin/env python


def get_bc(nums, m):
    """
    生成散列表： 坏字符在模式串中出现的位置 - 该散列表中存储的是怀字符串在模式串中的位置信息
    BC散列表：数组下标用 ascii 码表示，值是模式串位置
    :param nums: 模式串
    :param m: 模式串长度
    :return: 散列表

    """
    # 初始化 bc 为256个字符
    bc = [-1 for _ in range(256)]

    for i in range(m):
        bc[i] = -1

    for j in range(m):
        ascii = ord(nums[j])
        bc[ascii] = j
    print("散列表: ", bc)
    return bc

# 好后缀，找到子串的位置，找不到就找 prefix 为 true 的子串
# a d c a d c
#    后缀子串  suffix[k]=pos    prefix[k]
#         c   suffix[1]=2      prefix[1]=false
#       d c   suffix[2]=1      prefix[2]=false
#     a d c   suffix[3]=0      prefix[3]=true
#   c a d c   suffix[4]=-1     prefix[4]=false
# d c a d c   suffix[5]=-1     prefix[5]=false
def get_gs(m, size_m, suffix, prefix):
    # 计算好后缀出现在最后子串出现的位置
    # 赋初值suffix全为-1，prefix全为False
    for i in range(size_m):
        suffix[i] = -1
        prefix[i] = False
    k = size_m-1
    while k > 0:
        sub_size = size_m - k   # 后缀子串长度
        pos = k - sub_size      # 分割位置-后缀子串长度
        while pos >= 0:
            if m[pos:pos+sub_size] == m[k:k+sub_size]:
                suffix[sub_size] = pos
                if pos == 0 or m[0:sub_size] == m[k:k+sub_size]:    # *此时还要判断一下当前子串是否是模式串的前缀子串
                    prefix[sub_size] = True
                break  # 只要匹配到了，就退出当前循环，否则匹配到前面子串的话，移动位数会增多，可能会过多移动
            pos -= 1
        k -= 1


# 'a', 'b', 'd', 'a', 'd', 'c', 'a', 'd', 'c', 'b', 'a'
# 'a', 'd', 'c', 'a', 'd', 'c'
# 坏字符规则，可能会产生后退的情况，以上述例子：散列表中存放 d 的数据是后面 d 的位置，而第一轮循环我们需要移动模式串的情况，是需要匹配到前面 d 的情况
# 很显然，我们只有后面 d 的位置，所以会产生后退
def bm_bc(n, size_n, m, size_m):
    """
    使用坏字符规则，解决主串和模式串的匹配问题
    :param n: 主串
    :param m: 模式串
    :return: 主串和模式串匹配的第一个位置，没有匹配返回 -1
    """
    # bc 存储模式串每个字符存放的下标值
    # bc['a'] = 0
    # bc['d'] = 1
    # bc['c'] = 2
    bc = get_bc(m, size_m)
    i = 0

    while i < size_n - size_m:  # i 表示匹配的首位，从 0~size_n-size_m

        j = size_m-1            # j 表示从模式串尾开始匹配的下标
        while j >= 0:
            if n[i+j] != m[j]:  # 循环从字符串尾匹配，当出现坏字符串时，退出，记录 j 的值
                i += j - bc[ord(n[i+j])]  # 从散列表中找到坏字符的位置（字符串 n 中的坏字符在字符串 m 的位置，进而确定模式串移动多少）
                break
            else:
                j -= 1
        if j < 0:               # 当 j<0 时，说明模式串都已经被匹配
            print("模式串已经完全被匹配，位置在：", i)
            return i
    return -1


def bm(n, size_n, m, size_m):
    bc = get_bc(m, size_m)
    suffix = [-1 for _ in range(size_m)]
    prefix = [False for _ in range(size_m)]
    get_gs(m, size_m, suffix, prefix)
    print("suffix:", suffix)
    print("prefix:", prefix)

    i = 0
    while i < size_n - size_m:  # i 表示匹配的首位，从 0~size_n-size_m

        j = size_m-1            # j 表示从模式串尾开始匹配的下标
        while j >= 0:
            if n[i+j] != m[j]:
                # print("i, j, n[i+j], n[j]", i, j, n[i+j], n[j])
                # 此处发生字符不匹配
                # 坏字符规则 / 好后缀规则，选择移动位数多的那个规则
                # 坏字符串规则要移动的位数
                bc_move = j - bc[ord(n[i+j])]
                # 好后缀规则要移动的位数
                gs_move = 0
                r_pos = 0  # 记录好后缀的最长子串
                if j < size_m-1:  # 有好后缀的情况(j<size_m-1)
                    if suffix[size_m-1-j] != -1:  # 模式串存在与好后缀一致的另外一个子串
                        gs_move = j - suffix[size_m-1-j] + 1
                    else:      # 寻找好后缀子串匹配模式串前缀
                        for r in range(1, size_m-1-j):
                            if prefix[r] is True:
                                r_pos = r   # 记录最后的 True
                            gs_move = size_m-r_pos

                print("i, j, bc[ord(n[j])], bc_move, gs_move", i, j, bc[ord(n[j])], bc_move, gs_move)
                i += max(bc_move, gs_move)

            else:
                j -= 1
        if j < 0:               # 当 j<0 时，说明模式串都已经被匹配
            print("模式串已经完全被匹配，位置在：", i)
            return i
    return -1


if __name__ == '__main__':
    # 坏字符匹配（举例)
    # n = ['a', 'b', 'd', 'a', 'd', 'd', 'a', 'd', 'c', 'b', 'a']
    # m = ['a', 'd', 'c']
    # pos = bm(n, 11, m, 3)

    # 好后缀匹配（举例)
    # n = ['G','T','T','A','T','A','G','C','T','G','A','T','C','G','C','G','G','C','G','T','A','G','C','G','G','C','G','A','A']
    # m = ['G','T','A','G','C','G','G','C','G']
    n = "GTTATAGCTGATCGCGGCGTAGCGGCGAA"
    m = "GTAGCGGCG"
    pos = bm(n, 29, m, 9)

    print(pos)

    # suffix = [-1 for _ in range(6)]
    # prefix = [False for _ in range(6)]
    # generate_gs(['a', 'd', 'c', 'a', 'd', 'c'], 6, suffix, prefix)
    # print(suffix[1:])
    # print(prefix[1:])
