# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        def post_order(root):
            if not root:
                return
            post_order(root.left)
            post_order(root.right)
            res.append(root.val)

        res = []
        post_order(root)
        return res

    def postorderTraversal_no_recursion(self, root):
        res = []
        if not root:
            return res
        s1, s2 = [], []
        s1.append(root)
        while s1:
            T = s1.pop()
            s2.append(T)
            if T.left:
                s1.append(T.left)
            if T.right:
                s1.append(T.right)
        while s2:
            res.append(s2.pop().val)
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
    print(s.postorderTraversal(root))
    print(s.postorderTraversal_no_recursion(root))