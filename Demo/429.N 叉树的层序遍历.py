# -*- coding:utf-8 -*-
# !/usr/bin/env python

import collections

# 树结点类
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder_basic(self, root):
        """
        基础的层序遍历，就是把每一层的结点值一次性打印出来
        类似于 ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] 这样
        :param root:
        :return:
        """
        res = []
        queue = collections.deque()
        queue.appendleft(root)
        while(queue):
            pop_node = queue.pop()
            res.append(pop_node.val)
            for node in pop_node.children:
                queue.appendleft(node)
        return res





    def levelOrder(self, root):
        """
        层序遍历(LeetCode中规定的格式)，即把每一层的结点放进各自的数组中
        类似于[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H', 'I']] 这样
        :param root:
        :return:
        """
        # 最终结果
        res = []
        if not root:
            return res

        # 初始化队列，并且将根结点置入队列中
        # 存放每一个层级的结点
        queue = collections.deque()
        queue.appendleft(root)
        while(queue):
            # 临时存放结点的队列，最终合并到最后的 res 中
            tmp_res = []
            # 临时存放下一层结点的队列
            tmp_queue = []
            for node in queue:
                tmp_res.append(node.val)
                # 将孩子结点放置到 tmp_queue 中
                for child_node in node.children:
                    tmp_queue.append(child_node)
            queue = tmp_queue
            res.append(tmp_res)

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
    print(s.levelOrder_basic(root))
    print(s.levelOrder(root))

