# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# url:https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def pre_order(root):
            if not root:
                return
            res.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        res = []
        pre_order(root)
        return res

    def preorderTraversal_no_recursion(self, root):
        if not root:
            return []
        s = [root]      # 借助栈
        res = []        # 结果存放的位置
        while s:
            res.append(root.val)
            if root.right:
                s.append(root.right)
            if root.left:
                root = root.left
            else:
                root = s.pop()
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
    print(s.preorderTraversal(root))
    print(s.preorderTraversal_no_recursion(root))