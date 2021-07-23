# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        # 队列
        queue = [root]
        res = []
        while queue:    # 只要队列中有元素，就弹出，然后判断他的孩子结点。有孩子结点：入队；否则，继续弹出
            node = queue.pop(0)
            res.append(node.val)
            if node.children:
                for child_node in node.children:
                    queue.append(child_node)
        return res

    def levelOrder_leetcode(self, root):
        """
        题目要求：需要将每一行元素放置到一个list中去
        注意：将每一层单独放置时候的一个技巧点:
        每一层遍历的时候，让孩子结点临时入队，之后queue = tmp_queue，下一层进行新的一个queue的遍历，循环进行
        :param root:
        :return:
        """
        res = []
        queue = [root]
        if not root:
            return res
        while queue:
            level_queue = []  # 临时保存每一层结点元素便于下一次进行迭代
            level_res = []    # 临时保存每一层结点值
            for node in queue:
                level_res.append(node.val)
                if node.children:
                    for child_node in node.children:
                        level_queue.append(child_node)
            queue = level_queue
            res.append(level_res)
        return res




if __name__ == "__main__":
    # 新建节点
    root = Node('A')
    node_B = Node('B')
    node_C = Node('C')
    node_D = Node('D')
    node_E = Node('E')
    node_F = Node('F')
    node_G = Node('G')
    node_H = Node('H')
    node_I = Node('I')
    # 构建三叉树
    #        A
    #      / | \
    #     B  C  D
    #    /|\   / \
    #   E F G H   I
    root.children = [node_B, node_C, node_D]
    node_B.children = [node_E, node_F, node_G]
    node_D.children = [node_H, node_I]

    s = Solution()
    print(s.levelOrder(root))
    print(s.levelOrder_leetcode(root))
