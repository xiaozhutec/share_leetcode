# -*- coding:utf-8 -*-
# !/usr/bin/env python

def handle(list):
    size = len(list)
    print(size)
    for i in range(1, size-1):
        min_left = max(list[:i])
        max_right = min(list[i+1:])
        if min_left < list[i] < max_right:
            return list[i]
    return -1


print(handle([3, 5, 4, 2, 1, 6, 8, 7]))
