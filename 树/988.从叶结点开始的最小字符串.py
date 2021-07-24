# -*- coding:utf-8 -*-
# !/usr/bin/env python

import collections

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def smallestFromLeaf_dfs(self, root):
        res = []

        def dfs(root, path):
            if not root:
                return
            if root and not root.left and not root.right:
                res.append(str(chr(root.val + ord('a'))) + path)   # path一定要放在root.val后面，因为需要把子结点放在前面
            if root.left:
                dfs(root.left, str(chr(root.val + ord('a'))) + path)
            if root.right:
                dfs(root.right, str(chr(root.val + ord('a'))) + path)

        dfs(root, "")
        return min(res)

    def smallestFromLeaf_bfs(self, root):
        res = []
        if not root:
            return ""
        queue = collections.deque()
        queue.appendleft((root, chr(root.val + ord('a'))))
        while queue:
            node, node_val = queue.pop()
            if not node.left and not node.right:
                res.append(node_val)
            if node.left:
                queue.appendleft((node.left, chr(node.left.val + ord('a')) + node_val))
            if node.right:
                queue.appendleft((node.right, chr(node.right.val + ord('a')) + node_val))
        return min(res)


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
    node_I = TreeNode(20)
    node_J = TreeNode(9)
    # 构建二叉树
    #        5
    #      /   \
    #     3     2
    #    / \   / \
    #   1   2 4   9
    #  / \
    # 7   20
    #      \
    #       9
    root.left, root.right = node_B, node_C
    node_B.left, node_B.right = node_D, node_E
    node_C.left, node_C.right = node_F, node_G
    node_D.left, node_D.right = node_H, node_I
    node_I.right = node_J

    s = Solution()
    print(s.smallestFromLeaf_dfs(root))
    print(s.smallestFromLeaf_bfs(root))


# 0 1 2 3 4 5 6 7 8 9
# a b c d e f g h i j