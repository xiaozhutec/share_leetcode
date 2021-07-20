# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
import collections


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum_dfs(self, root, targetSum):
        """
        深度优先搜索处理
        1. 先序遍历到每个结点时，从该节点出发到下面结点所有路径的所有路径和进行比较，如果路径和==targetSum，则将该路径保存
        2，继续执行第 1 点
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return 0
        # 在这里原本数打印先序遍历结点的地方，进行向下所有路径的探索
        cnt = self.path_cnt(root, targetSum)
        left_cnt = self.pathSum_dfs(root.left, targetSum)
        right_cnt = self.pathSum_dfs(root.right, targetSum)
        return cnt + left_cnt + right_cnt

    def path_cnt(self, root, targetSum):
        if not root:
            return 0
        targetSum = targetSum - root.val
        cnt = 1 if targetSum == 0 else 0
        return cnt + self.path_cnt(root.left, targetSum) + self.path_cnt(root.right, targetSum)

    def pathSum_bfs(self, root, targetSum):
        """
        结点本身的遍历 和 遍历到当前结点去遍历向下所有路径的逻辑都采用 BFS 处理
        :param root:
        :param targetSum:
        :return:
        """
        cnt = 0
        if not root:
            return cnt
        queue = collections.deque()
        queue.appendleft(root)
        while queue:
            node = queue.pop()
            cnt += self.path_cnt_bfs(node, targetSum)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return cnt

    def path_cnt_bfs(self, root, targetSum):
        cnt = 0
        if not root:
            return 0
        queue = collections.deque()
        queue.appendleft((root, root.val))  # 元祖 (结点, 从根结点到当前结点的路径总和)
        while queue:
            node, node_val = queue.pop()
            if node_val == targetSum:
                cnt += 1
            if node.left:
                queue.appendleft((node.left, node_val + node.left.val))
            if node.right:
                queue.appendleft((node.right, node_val + node.right.val))
        return cnt



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
    print(s.pathSum_dfs(root, 11))
    print(s.pathSum_bfs(root, 11))