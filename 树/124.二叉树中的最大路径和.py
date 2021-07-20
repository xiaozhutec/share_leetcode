# -*- coding:utf-8 -*-
# !/usr/bin/env python

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        self.length = float("-inf")

        def dfs(root):
            if not root:
                return 0
            left_len = max(dfs(root.left), 0)   # 只有贡献值大于 0 的，才会选取对应的子结构
            right_len = max(dfs(root.right), 0)
            inner_max = left_len + root.val + right_len

            self.length = max(self.length, inner_max)   # 计算当前结点所在子树的最大路径
            return max(left_len, right_len) + root.val  # 返回当前结点左右子结构的最大路径

        dfs(root)
        return self.length


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
    print(s.maxPathSum(root))
