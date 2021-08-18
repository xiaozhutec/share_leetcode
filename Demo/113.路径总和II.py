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
    def pathSum_dfs(self, root, targetSum):
        if not root:
            return
        res = []

        def dfs(root, target_sum, path, res_path):
            """
            :param root: 当前根结点
            :param target_sum: 当前目标值
            :param path: 当前路径列表
            :param res_path: 当前最终结果路径列表
            :return:
            """
            if not root:
                return
            if not root.left and not root.right and target_sum == root.val:
                res_path.append(path + [root.val])
            dfs(root.left, target_sum - root.val, path + [root.val], res_path)
            dfs(root.right, target_sum - root.val, path + [root.val], res_path)

        dfs(root, targetSum, [], res)
        return res


    def pathSum_bfs(self, root, targetSum):
        if not root:
            return
        res = collections.deque() # 保存最后结果list
        queue = collections.deque()
        queue.appendleft((root, root.val, [root.val])) # (结点,根到当前结点累加和,根到当前结点路径)

        while(queue):
            node, node_val, node_path = queue.pop()
            if not node.left and not node.right and node_val == targetSum:
                res.appendleft(node_path)
            if node.left:
                queue.appendleft((node.left, node_val+node.left.val, node_path+[node.left.val]))
            if node.right:
                queue.appendleft((node.right, node_val+node.right.val, node_path+[node.right.val]))
        return list(res)




if __name__ == "__main__":
    # 新建节点
    root = TreeNode(5)
    node_B = TreeNode(3)
    node_C = TreeNode(6)
    node_D = TreeNode(1)
    node_E = TreeNode(2)
    node_F = TreeNode(5)
    node_G = TreeNode(9)
    node_H = TreeNode(7)
    node_I = TreeNode(0)
    node_J = TreeNode(9)
    # 构建二叉树
    #        5
    #      /   \
    #     3     6
    #    / \   / \
    #   1   2 5   9
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
    print(s.pathSum_dfs(root, 16))
    print(s.pathSum_bfs(root, 16))
