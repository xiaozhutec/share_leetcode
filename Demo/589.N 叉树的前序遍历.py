# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        # print(root.val, end=" ")
        # for node in root.children:
        #     self.preorder(node)

        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for node in root.children:
                dfs(node)
        dfs(root)
        return res



if __name__ == "__main__":
    # 新建节点
    root = Node('A')
    node_B = Node('B')
    node_C = Node('C')
    node_D = Node('D')
    node_E = Node('E')
    node_F = Node('F')
    node_G = Node('G')
    node_H = Node('H')
    node_I = Node('I')
    # 构建三叉树
    #        A
    #      / | \
    #     B  C  D
    #    /|\   / \
    #   E F G H   I
    root.children = [node_B, node_C, node_D]
    node_B.children = [node_E, node_F, node_G]
    node_D.children = [node_H, node_I]

    s = Solution()
    print(s.preorder(root))
