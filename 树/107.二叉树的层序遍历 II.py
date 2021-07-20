# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            tmp_queue = []
            tmp_res = []
            for node in queue:
                tmp_res.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)

            queue = tmp_queue
            res.insert(0, tmp_res) # 头部插入每一层list
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
    print(s.levelOrderBottom(root))
