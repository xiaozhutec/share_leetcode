# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def pre_order_traverse(self, head):
        """
        先序遍历
        :param head:
        :return:
        """
        if head is None:
            return
        print(head.value, end=" ")
        self.pre_order_traverse(head.left)
        self.pre_order_traverse(head.right)

    def in_order_traverse(self, head):
        """
        中序遍历
        :param head:
        :return:
        """
        if head is None:
            return
        self.in_order_traverse(head.left)
        print(head.value, end=" ")
        self.in_order_traverse(head.right)

    def post_order_traverse(self, head):
        """
        后续遍历
        :param head: 根结点
        :return:
        """
        if head is None:
            return
        self.post_order_traverse(head.left)
        self.post_order_traverse(head.right)
        print(head.value, end=" ")

    def level_order_traverse(self, head):
        """
        层次遍历
        i: 将头结点入队
        ii: 弹出队首元素，如果被弹出的队首元素有左右孩子，将它们一次入队
        iii: 循环第 ii 直到队列为空
        :param head: 根结点
        :return:
        """
        if not head:
            return
        queue = [head]
        while len(queue) > 0:
            tmp = queue.pop(0)
            print(tmp.value, end=" ")
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)

    # binary_tree_path - 神代码 - 看不懂
    def binaryTreePaths(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return [str(root.value)]
        paths = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                paths.append(str(root.value) + "->" + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                paths.append(str(root.value) + "->" + i)
        return paths

    def binaryTreePaths1(self, root):
        if not root:
            return []
        res = []

        def dfs(root, tmp):
            if not root:
                return

            # 1. 递归问题
            # 2. res 拼接问题
            # 如果是叶子节点，将 root.val 拼接到临时路径中
            if root and (root.left is None and root.right is None):
                res.append(tmp + str(root.value))
            print(res)
            # 如果当前节点不是叶子节点，将 root.val+"->" 拼接到临时路径中
            if root.left:
                dfs(root.left, tmp + str(root.value) + "->")
            # 如果当前节点不是叶子节点，将 root.val+"->" 拼接到临时路径中
            if root.right:
                dfs(root.right, tmp + str(root.value) + '->')

        dfs(root, "")
        return res

    def maxDepth_dfs(self, root):
        """
        104. 二叉树的最大深度
        DFS 求解
        :param root: 根结点
        :return:
        """
        if not root:
            return 0
        else:
            left_max = self.maxDepth_dfs(root.left)
            right_max = self.maxDepth_dfs(root.right)
            return max(left_max, right_max) + 1

    def maxDepth_bfs(self, root):
        """
        104. 二叉树的最大深度
        BFS 求解
        层次遍历变种，循环将每层出队并且孩子入队的操作，深度+1
        :param root: 根结点
        :return:
        """
        max_depth = 0
        queue = [root]
        if not root:
            return max_depth

        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            max_depth += 1
        return max_depth


if __name__ == "__main__":
    # 新建节点
    node_A = TreeNode(-10)
    node_B = TreeNode(9)
    node_C = TreeNode(20)
    node_D = TreeNode(18)
    node_E = TreeNode(1)
    node_F = TreeNode(-3)
    node_G = TreeNode(2)
    node_H = TreeNode(-7)

    # 构建二叉树
    #     -10
    #    /   \
    #   9     20
    #  /     / \
    # 18    1   -3
    #      / \
    #     2  -7

    node_A.left, node_A.right = node_B, node_C
    node_B.left = node_D
    node_C.left, node_C.right = node_E, node_F
    node_E.left, node_E.right = node_G, node_H

    s = Solution()
    # 打印结点元素
    print("先序遍历结果：")
    s.pre_order_traverse(node_A)
    print("\n中序遍历结果：")
    s.in_order_traverse(node_A)
    print("\n后续遍历结果：")
    s.post_order_traverse(node_A)
    print("\n二叉树层次遍历：")
    s.level_order_traverse(node_A)
    print("\n树的最大深度DFS：")
    print(s.maxDepth_dfs(node_A))
    print("\n树的最大深度BFS：")
    print(s.maxDepth_bfs(node_A))
    print("\n二叉树的所有路径：")
    print(s.binaryTreePaths(node_A))

    print("+++++++++++")
    print(s.binaryTreePaths1(node_A))
