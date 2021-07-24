# -*- coding:utf-8 -*-
# !/usr/bin/env python

import collections

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers_dfs(self, root):
        res = []    # 所有路径集合
        sum = 0     # 所有路径求和

        def dfs(root, path):
            if not root:
                return
            if root and not root.left and not root.right:
                res.append(path + str(root.val))
            if root.left:
                dfs(root.left, path + str(root.val))
            if root.right:
                dfs(root.right, path + str(root.val))

        dfs(root, "")
        for item in res:
            sum += int(item)

        return sum

    def sumNumbers_bfs(self, root):
        res = []
        sum = 0
        if not root:
            return 0
        queue = collections.deque()
        queue.append((root, str(root.val)))
        while queue:
            node, node_val = queue.pop()
            if node and not node.left and not node.right:
                res.append(node_val)
            if node.left:
                queue.appendleft((node.left, node_val+str(node.left.val)))
            if node.right:
                queue.appendleft((node.right, node_val+str(node.right.val)))
        for item in res:
            sum += int(item)
        return sum


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
    print(s.sumNumbers_dfs(root))
    print(s.sumNumbers_bfs(root))
