# -*- coding:utf-8 -*-
# !/usr/bin/env python

import collections


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root.val


if __name__ == "__main__":
    # 新建节点
    root = TreeNode(9)
    node_B = TreeNode(8)
    node_C = TreeNode(18)
    node_D = TreeNode(1)
    node_E = TreeNode(9)
    node_F = TreeNode(11)
    node_G = TreeNode(20)
    node_H = TreeNode(0)
    node_I = TreeNode(2)
    node_J = TreeNode(3)
    # 构建二叉树
    #        9
    #      /   \
    #     8     18
    #    / \   / \
    #   1   9 11  20
    #  / \
    # 0   2
    #      \
    #       3
    root.left, root.right = node_B, node_C
    node_B.left, node_B.right = node_D, node_E
    node_C.left, node_C.right = node_F, node_G
    node_D.left, node_D.right = node_H, node_I
    node_I.right = node_J

    s = Solution()
    print(s.lowestCommonAncestor(root, node_H, node_J))
