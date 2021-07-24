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

    def pathSum(self, root, targetSum):
        """
        递归解决
        要同时存储递归到每一个结点的「路径和」，「路径list值」
        :param root: 根结点
        :param targetSum: 目标计算值
        :return: 路径list
        """
        res = []

        def dfs(root, sum, node_path, res_list):
            """
            :param root: 根结点
            :param sum: 目标总和
            :param node_path: 根结点到当前结点的路径list
            :param res_list: 返回结果列表
            :return: res
            """
            if not root:
                return
            if not root.left and not root.right and sum == root.val:
                res_list.append(node_path + [root.val])
            dfs(root.left, sum - root.val, node_path + [root.val], res_list)
            dfs(root.right, sum - root.val, node_path + [root.val], res_list)

        dfs(root, targetSum, [], res)
        return res

    # 还是要注意 if not root: return 最后的意义

    def pathSum_bfs(self, root, targetSum):
        res = []
        if not root:
            return res
        # 三元组 (结点、根结点到当前结点的路径和、根结点到当前结点的路径list)
        queue = [(root, root.val, [root.val])]
        while queue:
            node, node_val, node_list = queue.pop(0)
            if not node.left and not node.right and node_val == targetSum:
                res.append(node_list)
            if node.left:
                queue.append((node.left, node.left.val + node_val, node_list + [node.left.val]))
            if node.right:
                queue.append((node.right, node.right.val + node_val, node_list + [node.right.val]))
        return res

    def pathSum_bfs_s(self, root, targetSum):
        """
        运用了 Collections 包，执行效率较高
        :param root:
        :param targetSum:
        :return:
        """
        res = []
        if not root:
            return []
        queue = collections.deque()
        queue.appendleft((root, root.val, [root.val]))
        while queue:
            node, node_val, node_list = queue.pop()
            if not node.left and not node.right and node_val == targetSum:
                res.append(node_list)
            if node.left:
                queue.appendleft((node.left, node.left.val + node_val, node_list + [node.left.val]))
            if node.right:
                queue.appendleft((node.right, node.right.val + node_val, node_list + [node.right.val]))
        return res


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
    print(s.pathSum(root, 16))
    print(s.pathSum_bfs(root, 16))
    print(s.pathSum_bfs_s(root, 16))