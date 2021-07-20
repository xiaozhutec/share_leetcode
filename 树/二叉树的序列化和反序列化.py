# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class TreeSerializeAndDeserialize(object):

    def __init__(self):
        # 二叉树序列化后字符串结果
        self.serialize_string = ""

    def print_tree_pre_order_traverse(self, head):
        if head is None:
            return None
        print(head.val, end=" ")
        self.print_tree_pre_order_traverse(head.left)
        self.print_tree_pre_order_traverse(head.right)

    def create_tree(self, item_tree_node):
        if len(item_tree_node) <= 0:
            return None
        item = item_tree_node.pop(0)
        root = None
        if item != '#':
            root = TreeNode(item)
            root.left = self.create_tree(item_tree_node)
            root.right = self.create_tree(item_tree_node)
        return root

    # 先序实现序列化
    def serialize_by_pre_order_traverse(self, root):
        # 说明：序列化二叉树，在序列化的同时，每遍历一个值，在该值后面加!(叹号)，空节点用#(井号)表示
        # !(叹号) 的作用是：表示该节点内容结束，例如：如果不加!(叹号)，88表示8还是88，就会有歧义了
        # #(井号) 的作用是：表示结点为空结点，为了保持逻辑一致性，空节点也也用#!表示。其实也可以直接用#表示
        # 二叉树结构：
        #      6
        #    /   \
        #  88     92
        #  /      / \
        # 10     11  12
        #       / \
        #      22  9
        # 先序序列化：6!88!10!#!#!#!92!11!22!#!#!9!#!#!12!#!#!
        if root is None:
            self.serialize_string += "#!"
            return None
        self.serialize_string += root.val+"!"
        self.serialize_by_pre_order_traverse(root.left)
        self.serialize_by_pre_order_traverse(root.right)
    
    # 先序实现反序列化
    def deserialize_by_pre_order_traverse(self, serialize_string):
        items_tree_node = []
        items = serialize_string.split("!")[0:-1]
        # 将各个结点值放置到 list 中
        for item in items:
            items_tree_node.append(item)
        # print(items_tree_node)
        # 构造二叉树
        return self.create_tree(items_tree_node)


if __name__ == "__main__":
    # 新建节点
    node_A = TreeNode("6")
    node_B = TreeNode("88")
    node_C = TreeNode("92")
    node_D = TreeNode("10")
    node_E = TreeNode("11")
    node_F = TreeNode("12")
    node_G = TreeNode("22")
    node_H = TreeNode("9")

    # 构建二叉树
    #      6
    #    /   \
    #  88     92
    #  /      / \
    # 10     11  12
    #       / \
    #      22  9

    node_A.left, node_A.right = node_B, node_C
    node_B.left = node_D
    node_C.left, node_C.right = node_E, node_F
    node_E.left, node_E.right = node_G, node_H

    serialize_res = ""
    # 实例化类
    TS = TreeSerializeAndDeserialize()
    print("\n先序遍历树结构: ")
    TS.print_tree_pre_order_traverse(node_A)

    # 利用先序遍历进行序列化
    TS.serialize_by_pre_order_traverse(node_A)
    print("\n通过先序遍历进行序列化：\n", TS.serialize_string)

    # 利用先序遍历进行反序列化
    print("通过先序遍历进行反序列化：")
    TS.deserialize_head = TS.deserialize_by_pre_order_traverse(TS.serialize_string)
    TS.print_tree_pre_order_traverse(TS.deserialize_head)
