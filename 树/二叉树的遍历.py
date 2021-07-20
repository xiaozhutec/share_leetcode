# -*- coding:utf-8 -*-
# !/usr/bin/env python

# 树结点类
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:

    def pre_order_traverse(self, root):
        """
        先序遍历-递归
        :param root: 根结点
        :return:
        """
        if not root:
            return
        print(root.value, end=" ")
        self.pre_order_traverse(root.left)
        self.pre_order_traverse(root.right)

    def pre_order_traverse_no_recursion(self, root):
        """
        先序遍历-非递归-利用堆栈「访问根结点，右孩子压栈，左孩子打印」
        1. 访问根结点。
        2. 判断是否有右孩子，如果有右孩子，压栈
        3. 判断否则有左孩子，如果有左孩子，访问它，否则，弹出栈顶元素
        4. 循环执行 2 和 3
        :param root: 根结点
        :return:
        """
        if not root:
            return
        stack = [root]
        while stack:
            print(root.value, end=" ")  # 访问根结点
            if root.right:
                stack.append(root.right)  # 判断是否有右孩子，如果有右孩子，压栈
            if root.left:  # 判断否则有左孩子，如果有左孩子，访问它，否则，弹出栈顶元素
                root = root.left
            else:
                root = stack.pop()

    def in_order_traverse(self, root):
        """
        中序遍历-递归
        :param root: 根结点
        :return:
        """
        if not root:
            return
        self.in_order_traverse(root.left)
        print(root.value, end=" ")
        self.in_order_traverse(root.right)

    def in_order_traverse_no_recursion(self, root):
        """
        中序遍历-非递归 「左压栈，弹出向右再左压栈」
        1. 当遍历到一个结点时，就压栈，然后继续去遍历它的左子树;
        2. 当左子树遍历完成后，从栈顶弹出栈顶元素（左子树最后一个元素）并访问它;
        3. 最后按照当前指正的右孩子继续中序遍历，若没有右孩子，继续弹出栈顶元素。
        :param root: 根结点
        :return:
        """
        if not root:
            return
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                tmp = stack.pop()
                print(tmp.value, end=" ")
                root = tmp.right

    def post_order_traverse(self, root):
        """
        后续遍历-递归
        :param root: 根结点
        :return:
        """
        if not root:
            return
        self.post_order_traverse(root.left)
        self.post_order_traverse(root.right)
        print(root.value, end=" ")

    def post_order_traverse_no_recursion1(self, root):
        """
        后续遍历-非递归-借助2个栈：s1 和 s2
        1. 初始化根结点到s1中
        2. 将 s1 栈顶元素 T 弹出，到栈 s2 中
        3. 判断 T 是否有左右孩子，如果有依次入栈 s1，否则，执行第 2 条
        :param root: 根结点
        :return:
        """
        s1, s2 = [], []
        s1.append(root)             # 初始化根结点到S1中
        while s1:
            T = s1.pop()            # 将 S1 栈顶元素 T 弹出，到栈 S2 中
            s2.append(T)
            if T.left:              # 判断 T 是否有左右孩子，如果有依次入栈 s1
                s1.append(T.left)
            if T.right:
                s1.append(T.right)
        while s2:
            print(s2.pop().value, end=" ")

    def post_order_traverse_no_recursion2(self, root):
        """
        后续遍历-非递归-借助1个栈
        :param root: 根结点
        :return:
        """
        pass

    def level_order_traverse(self, head):
        """
        层次遍历 - 「结点出队、访问该结点、其左右儿子入队，直到结点为空」
        1. 将头结点入队
        2. 弹出队首元素，如果被弹出的队首元素有左右孩子，将它们一次入队
        3. 循环第 ii 直到队列为空
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
    print("\n先序遍历-递归：")
    s.pre_order_traverse(root)
    print("\n先序遍历-非递归：")
    s.pre_order_traverse_no_recursion(root)
    print("\n中序遍历-递归：")
    s.in_order_traverse(root)
    print("\n中序遍历-非递归：")
    s.in_order_traverse_no_recursion(root)
    print("\n后序遍历-递归：")
    s.post_order_traverse(root)
    print("\n后序遍历-非递归(方法一)：")
    s.post_order_traverse_no_recursion1(root)
    print("\n层次遍历")
    s.level_order_traverse(root)