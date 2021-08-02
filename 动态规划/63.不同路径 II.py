# -*- coding:utf-8 -*-
# !/usr/bin/env python

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # 在 0 行 0 列处有障碍物的话，无法走动，直接返回 0
        if obstacleGrid[0][0] == 1:
            return 0

        # 否则，位置(0, 0)可以到达
        obstacleGrid[0][0] = 1

        # 初始化 0 列
        for clo in range(1, m):
            obstacleGrid[clo][0] = int(obstacleGrid[clo][0] == 0 and obstacleGrid[clo-1][0] == 1)

        # 初始化 0 行
        for row in range(1, n):
            obstacleGrid[0][row] = int(obstacleGrid[0][row] == 0 and obstacleGrid[0][row-1] == 1)
        print(obstacleGrid)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
