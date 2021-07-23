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
    def hasPathSum(self, root, targetSum):
        """
        给你二叉树的根节点root 和一个表示目标和的整数targetSum
        判断该树中是否存在 根节点到叶子节点 的路径
        这条路径上所有节点值相加等于目标和targetSum

        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum_bfs(self, root, targetSum):
        """
        利用 BFS 的方式进行计算
        每遍历到一个结点，保存根结点到该结点的路径总和
        并且同时判断该结点是否为叶子结点，如果是，那么和 targetSum 做比较，如果不是，继续访问下一个结点，知道全部访问完毕
        :param root: 根结点
        :param targetSum: 目标值
        :return:
        """
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            node, node_sum = queue.pop(0)
            if not node.left and not node.right and node_sum == targetSum:
                return True
            if node.left:
                queue.append((node.left, node_sum+node.left.val))
            if node.right:
                queue.append((node.right, node_sum+node.right.val))
        return False

    def hasPathSum_bfs_s(self, root, targetSum):
        if not root:
            return False
        queue = collections.deque()
        queue.appendleft((root, root.val))
        while queue:
            node, node_sum = queue.pop()
            if not node.left and not node.right and node_sum == targetSum:
                return True
            if node.left:
                queue.appendleft((node.left, node_sum+node.left.val))
            if node.right:
                queue.appendleft((node.right, node_sum+node.right.val))
        return False


if __name__ == "__main__":
    # 新建节点
    root = TreeNode(5)
    node_B = TreeNode(3)
    node_C = TreeNode(6)
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
    #     3     6
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
    print(s.hasPathSum(root, 18))
    print(s.hasPathSum_bfs(root, 18))
    print(s.hasPathSum_bfs_s(root, 18))