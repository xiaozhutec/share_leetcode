#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import subprocess
import random


def readin_itemDic2():
    d = {}

    cat = subprocess.Popen(["cat", './online_upitem_dic'], stdout=subprocess.PIPE)
    for line in cat.stdout:
        v = line[0:-1].split('\t')
        try:
            d[v[0]] = v[1]
        except:
            pass
    return d


def readin_local():
    d = {}
    with open('./online_upitem_dic') as f:
        for line in f:
            v = line[0:-1].split('\t')
            if v[0] not in d:
                d[v[0]] = [v[1]]
            else:
                d[v[0]].append(v[1])
    return d


def readin_local2():
    d = {}

    with open('./online_upitem_dic') as f:
        for line in f:

            v = line[0:-1].split('\t')
            try:
                d[v[0]] = v[1]
            except:
                pass
    return d


os = sys.argv[1]
d = readin_itemDic2()
# d = readin_local2()

drop_out2 = ['110', '109', '113', '118', '120', '112', '111', '121']
drop_out = ['101', '102', '103', '105', '107', '114', '108', '117']
addi = ['112', '104', '114', '117']

for line in sys.stdin:
    v = line[0:-1].split("\t")
    devid = v[0]

    try:
        sys.argv[2]
        m = random.sample([str(x) for x in range(101, 122)], random.randint(3, 17))
    except:
        datas = v[1]
        r = set(map(lambda x: d[x] if x in datas else 'A', d))
        r.remove('A')

        m = r
        k = random.randint(0, 25)
        if k > 8 and len(r) > 8 and (os == 'imei' or os == 'gid_android'):
            c = set(random.sample(drop_out, random.randint(len(drop_out) / 2, len(drop_out)))) | set(
                random.sample(drop_out2, 2))
            m = r - c

        if len(r) < 7 and k > 8 and (os == 'idfa' or os == 'gid_ios'):
            m = r | set(addi)

    res = ','.join(m)
    print(devid + '\t' + res)
