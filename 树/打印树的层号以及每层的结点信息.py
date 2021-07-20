# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def level_order_traverse(root):
    if not root:
        return
        # 队列queue
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def level_order_traverse_datail(root):
    last, n_last = root, root
    i = 1
    if not root:
        return
    # 队列queue
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            n_last = node.left
            queue.append(node.left)
        if node.right:
            n_last = node.right
            queue.append(node.right)
        # 当弹出的结点是last指向的结点时，令 last = n_last
        if last is node:
            last = n_last
            print(" -> 第 %d 行" % i)
            i = i + 1


if __name__ == "__main__":
    # 新建节点
    node_A = TreeNode("A")
    node_B = TreeNode("B")
    node_C = TreeNode("C")
    node_D = TreeNode("D")
    node_E = TreeNode("E")
    node_F = TreeNode("F")
    node_G = TreeNode("G")
    node_H = TreeNode("H")

    # 构建二叉树
    #      A
    #    /   \
    #   B     C
    #  /     / \
    # D     E   F
    #      / \
    #     G   H

    node_A.left, node_A.right = node_B, node_C
    node_B.left = node_D
    node_C.left, node_C.right = node_E, node_F
    node_E.left, node_E.right = node_G, node_H

    # 打印结点元素
    print("层次遍历结果：")
    level_order_traverse(node_A)

    print("\n层次遍历结果(打印行号)：")
    level_order_traverse_datail(node_A)