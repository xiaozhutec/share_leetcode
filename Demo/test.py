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
    def levelOrder(self, root):
        res = []
        queue = collections.deque()
        queue.appendleft((root, root.val, root.val))
        while queue:
            node, node_path, node_val = queue.pop()
            res.append((node, node_path, node_val))
            if node.left:
                queue.appendleft((node.left, node_path+str(node.left), node_val+node.left.val))
            if node.right:
                queue.appendleft((node.right, node_path+str(node.right), node_val+node.right.val))
        return res


if __name__ == "__main__":
    # 新建节点
    root = TreeNode('1')
    node_B = TreeNode('2')
    node_C = TreeNode('3')
    node_D = TreeNode('4')
    node_E = TreeNode('5')
    node_F = TreeNode('6')
    node_G = TreeNode('7')
    node_H = TreeNode('8')
    node_I = TreeNode('9')
    # 构建二叉树
    #        A
    #      /   \
    #     B     C
    #    / \   / \
    #   D   E F   G
    #  / \
    # H   I
    root.left, root.right = node_B, node_C
    node_B.left, node_B.right = node_D, node_E
    node_C.left, node_C.right = node_F, node_G
    node_D.left, node_D.right = node_H, node_I

    s = Solution()
    print(s.levelOrder(root))
