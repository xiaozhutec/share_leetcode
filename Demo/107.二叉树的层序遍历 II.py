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
    def levelOrderBottom(self, root):
        res = []
        queue = collections.deque()
        queue.appendleft(root)
        while(queue):
            level_queue = []   # 记录下一层的结点值
            level_res = []     # 记录当前层的结点值
            for node in queue:
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
                level_res.append(node.val)
            # 将下一层的结点都入到queue中，进行下一层的遍历
            queue = level_queue
            res.insert(0, level_res)
        return list(res)




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
    print(s.levelOrderBottom(root))
