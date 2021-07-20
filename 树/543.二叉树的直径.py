# -*- coding:utf-8 -*-
# !/usr/bin/env python

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.path_length = 0

        def dfs(root):
            if not root:
                return 0
            left_len = dfs(root.left)
            right_len = dfs(root.right)
            left_tag = right_tag = 0
            if root.left:
                left_tag = left_len + 1
            if root.right:
                right_tag = right_len + 1
            self.path_length = max(self.path_length, left_tag + right_tag)
            return max(left_tag, right_tag)

        dfs(root)
        return self.path_length


if __name__ == "__main__":
    # 新建节点
    root = TreeNode(5)
    node_B = TreeNode(3)
    node_C = TreeNode(2)
    node_D = TreeNode(1)
    node_E = TreeNode(2)
    node_F = TreeNode(4)
    node_G = TreeNode(9)
    node_H = TreeNode(7)
    node_I = TreeNode(0)
    node_J = TreeNode(9)
    # 构建二叉树
    #        5
    #      /   \
    #     3     2
    #    / \   / \
    #   1   2 4   9
    #  / \
    # 7   0
    #      \
    #       9
    root.left, root.right = node_B, node_C
    node_B.left, node_B.right = node_D, node_E
    node_C.left, node_C.right = node_F, node_G
    node_D.left, node_D.right = node_H, node_I
    node_I.right = node_J

    s = Solution()
    print(s.diameterOfBinaryTree(root))
