# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
import collections


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestUnivaluePath_dfs(self, root):
        self.length = 0

        def dfs(root):
            if not root:
                return 0
            left_len = dfs(root.left)
            right_len = dfs(root.right)
            left_tag = right_tag = 0
            if root.left and root.left.val == root.val:
                left_tag = left_len + 1
            if root.right and root.right.val == root.val:
                right_tag = right_len + 1
            print("length", self.length, "node:", root.val, "left_tag:", left_tag, "right_tag:", right_tag)
            # max(最大长度, 左子树最大长度+右子树最大长度)
            self.length = max(self.length, left_tag + right_tag)
            return max(left_tag, right_tag)

        dfs(root)
        return self.length


if __name__ == "__main__":
    # 新建节点
    root = TreeNode(5)
    node_B = TreeNode(5)
    node_C = TreeNode(2)
    node_D = TreeNode(5)
    node_E = TreeNode(2)
    node_F = TreeNode(4)
    node_G = TreeNode(9)
    node_H = TreeNode(5)
    node_I = TreeNode(5)
    node_J = TreeNode(5)
    node_K = TreeNode(5)
    # 构建二叉树
    #          5
    #        /   \
    #       5     2
    #      / \   / \
    #     5   2 4   9
    #    / \
    #   5   5
    #  /     \
    # 5       5
    root.left, root.right = node_B, node_C
    node_B.left, node_B.right = node_D, node_E
    node_C.left, node_C.right = node_F, node_G
    node_D.left, node_D.right = node_H, node_I
    node_H.left = node_J
    node_I.right = node_K

    s = Solution()
    print(s.longestUnivaluePath_dfs(root))
