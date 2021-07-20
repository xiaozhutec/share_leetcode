# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):

    def postorder(self, root):
        # 保存结点
        res = []
        def post_order(root):
            if not root:
                return
            for node in root.children:
                post_order(node)
            res.append(root.val)

        post_order(root)
        return res
