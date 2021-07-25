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
    def maxDepth_dfs(self, root):
        if not root:
            return 0
        else:
            max_left = self.maxDepth_dfs(root.left)
            max_right = self.maxDepth_dfs(root.right)
            return max(max_left, max_right) + 1

    def maxDepth_bfs(self, root):
        if not root:
            return 0
        queue = collections.deque()
        # 初始化深度为 0
        node_depth = 0
        # 初始化队列中的结点元素 root
        queue.appendleft(root)
        while queue:
            # 每一层的遍历，深度 +1
            node_depth += 1
            # 记录每一层的结点集合
            level_queue = []
            for node in queue:
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            queue = level_queue

        return node_depth


if __name__ == "__main__":
    # 新建节点
    root = TreeNode('A')
    node_B = TreeNode('B')
    node_C = TreeNode('C')
    node_D = TreeNode('D')
    node_E = TreeNode('E')
    node_F = TreeNode('F')
    node_G = TreeNode('G')
    node_H = TreeNode('H')
    node_I = TreeNode('I')
    node_J = TreeNode('J')
    # 构建二叉树
    #        A
    #      /   \
    #     B     C
    #    / \   / \
    #   D   E F   G
    #  / \
    # H   I
    #      \
    #       J
    root.left, root.right = node_B, node_C
    node_B.left, node_B.right = node_D, node_E
    node_C.left, node_C.right = node_F, node_G
    node_D.left, node_D.right = node_H, node_I
    node_I.right = node_J

    s = Solution()
    print(s.maxDepth_dfs(root))
    print(s.maxDepth_bfs(root))