# -*- coding:utf-8 -*-
# !/usr/bin/env python

import collections

# 树结点类
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

    def hasPathSum_bfs(self, root, targetSum):
        if not root:
            return False
        queue = collections.deque()
        # 使用元祖存放结点信息(结点,当前结点自顶向下路径和)
        queue.append((root, root.val))
        while queue:
            node, node_val = queue.pop()
            if not node.left and not node.right and node_val == targetSum:
                return True
            if node.left:
                queue.appendleft((node.left, node.left.val + node_val))
            if node.right:
                queue.appendleft((node.right, node.right.val + node_val))
        return False


if __name__ == "__main__":
    # 新建节点
    root = TreeNode(5)
    node_B = TreeNode(3)
    node_C = TreeNode(6)
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
    #     3     6
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
    print(s.hasPathSum(root, 18))
    print(s.hasPathSum_bfs(root, 18))
