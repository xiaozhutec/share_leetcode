# -*- coding:utf-8 -*-
# !/usr/bin/env python
import heapq
import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        字符串数组：[12, -3, 1, -1, 9, 5], 窗口大小：3
        利用优先队列解决：
        首先，初始化优先队列 [(-12, 0), (3, 1), (-1, 2)]，将最大值（12）插入到结果集res中
        然后，判断当前大顶堆最大值是否在窗口内（窗口利用下标进行记录）
        下面，开始每一步的进行窗口向右移动，并且将向右移动纳入的新值，插入到优先队列中。
        得到：
        [(-12, 0), (1, 3), (-1, 2), (3, 1)]
        此时要判断最大值 window 窗口： 1 3，所以需要将队首pop()
        [(-1, 2), (1, 3), (3, 1)]
        加入新值：
        [(-9, 4), (-1, 2), (3, 1), (1, 3)]
        此时要判断最大值 window 窗口： 2 4
        [(-9, 4), (-1, 2), (3, 1), (1, 3)]
        加入新值：
        [(-9, 4), (-5, 5), (3, 1), (1, 3), (-1, 2)]
        此时要判断最大值 window 窗口： 3 5
        [(-9, 4), (-5, 5), (3, 1), (1, 3), (-1, 2)]
        """
        size = len(nums)
        window = [(-nums[i], i) for i in range(k)]
        heapq.heapify(window)
        res = [-window[0][0]]
        print(window)

        for i in range(k, size):
            heapq.heappush(window, (-nums[i], i))
            print(window)
            print("window窗口：", i-k+1, i)
            while window[0][1] <= i-k:
                heapq.heappop(window)
            print(window)
            res.append(-window[0][0])
        return res

    def maxSlidingWindow1(self, nums, k):
        """
        利用双向队列，双向队列即入队和出队两头都可以进行
        使用 [12, -3, 1, -1, 9, 5] 举例：
        初始化一个空队列 queue=[]，存放下标（左队首，右队尾）
        结果集合 res=[]，存放窗口最大值
        第一点：如果入队的元素小于队尾元素，则直接入队；否则，队尾元素出队，直到入队元素小于队尾元素，如果一直出队至队列为空，则入队元素直接入队
        第二点：第一点保证了队首元素是整个队列中的最大值，但要主要队首元素现在不一定是在窗口内，这一点此时要做一个判断
        数组：[12, -3, 1, -1, 9, 5]
        下标：[0    1  2   3  4  5]
        ① queue=[0],item=[12],window=[0,0]          ---> 队列为空，直接插入到queue
        ② queue=[0,1],item=[12,-3],window=[0,1]     ---> -3<12，直接插入到queue
        ③ queue=[0,2],item=[12,1],window=[0,2]      ---> k=3，窗口形成，因1>-3，故-3出队，1入队。res=nums[queue[0]]=12
        ④ queue=[2,3],item=[1,-1],window=[1,3]      ---> 因-1<1，-1入队。下标0不在窗口[1,3]内，queue[0]出队。res=nums[queue[0]]=1
        ⑤ queue=[4],item=[9],window=[2,4]           ---> 因9大于所有的元素，所有都出队，9入队。res=nums[queue[0]]=9
        ⑥ queue=[4,5],item=[9,5],window=[3,5]       ---> 因5<9，5入队。res=nums[queue[0]]=9
        所有步骤执行完，res=[12,1,9,9]
        """
        size = len(nums)
        queue = collections.deque()
        res = []
        for i in range(0, size):
            # 新元素进队，在队不空的情况下，需要判断与队尾元素的大小
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            # 在已经形成窗口(i+1>=k)的前提下，判断队首是否在窗口内
            while queue[0] < i-k+1:
                queue.popleft()
            # 从形成窗口的时刻开始将元素置于结果集 res 中
            if i+1 >= k:
                res.append(nums[queue[0]])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([12, -3, 1, -1, 9, 5], 3))
    # print(s.maxSlidingWindow1([12, -3, 1, -1, 9, 5], 3))
