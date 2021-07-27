# -*- coding:utf-8 -*-
# !/usr/bin/env python

import collections

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def findDuplicateSubtrees(self, root):
        d = collections.defaultdict(list)

        def find(root):
            if not root:
                return ''
            left_chlid = find(root.left)
            right_chlid = find(root.right)
            s = ' '.join((str(root.val), left_chlid, right_chlid))
            d[s].append(root)
            return s

        find(root)
        return [l[0].val for l in d.values() if len(l) > 1]


if __name__ == "__main__":
    # 新建节点
    root = TreeNode(5)
    node_B = TreeNode(3)
    node_C = TreeNode(2)
    node_D = TreeNode(3)
    node_E = TreeNode(2)
    node_F = TreeNode(4)
    node_G = TreeNode(9)
    node_H = TreeNode(7)
    node_I = TreeNode(2)
    node_J = TreeNode(9)
    # 构建二叉树
    #        5
    #      /   \
    #     3     2
    #    / \   / \
    #   3   2 4   9
    #  / \
    # 7   2
    #      \
    #       9
    root.left, root.right = node_B, node_C
    node_B.left, node_B.right = node_D, node_E
    node_C.left, node_C.right = node_F, node_G
    node_D.left, node_D.right = node_H, node_I
    node_I.right = node_J

    s = Solution()
    print(s.findDuplicateSubtrees(root))
