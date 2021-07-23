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
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

        return res



    def levelOrder_lc(self, root):
        """
        题目要求：需要将每一行元素放置到一个list中去
        注意：将每一层单独放置时候的一个技巧点:
        每一层遍历的时候，让孩子结点临时入队，之后queue = tmp_queue，下一层进行新的一个queue的遍历，循环进行
        :param root:
        :return:
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            tmp_queue = []      # 临时记录每一层结点
            tmp_res = []        # 临时记录每一行的结点值
            for node in queue:
                tmp_res.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            queue = tmp_queue
            res.append(tmp_res)
        return res


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
    print(s.levelOrder(root))
    print(s.levelOrder_lc(root))