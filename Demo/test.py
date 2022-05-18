# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 好后缀，找到子串的位置，找不到就找 prefix 为 true 的子串
# a d c a d c
#    后缀子串  suffix[k]=pos    prefix[k]
#         c   suffix[1]=2      prefix[1]=false
#       d c   suffix[2]=1      prefix[2]=false
#     a d c   suffix[3]=0      prefix[3]=true
#   c a d c   suffix[4]=-1     prefix[4]=false
# d c a d c   suffix[5]=-1     prefix[5]=false
def generate_gs(m, size_m, suffix, prefix):
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
                print(m[0:sub_size], m[k:k+sub_size])
                if pos == 0 or m[0:sub_size] == m[k:k+sub_size]:    # *此时还要判断一下当前子串是否是模式串的前缀子串
                    prefix[sub_size] = True
                break
            pos -= 1
        k -= 1


suffix=[-1, -1, -1, -1, -1, -1, -1, -1, -1]
prefix=[False, False, False, False, False, False, False, False, False]
generate_gs(['G', 'T', 'A', 'G', 'C', 'G', 'G', 'C', 'G'], 9, suffix, prefix)
print(suffix)
print(prefix)



# suffix=[-1, -1, -1, -1, -1, -1]
# prefix=[False, False, False, False, False, False]
# generate_gs(['a', 'd', 'c', 'a', 'd', 'c'], 6, suffix, prefix)
# print(suffix)
# print(prefix)
