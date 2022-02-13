#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 64. 最小路径和
# https://leetcode-cn.com/problems/minimum-path-sum/
# 思路：dp， dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, columns):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        for i in range(rows):
            print(" ".join(str(dp[i])))

        return dp[rows-1][columns-1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = Solution().minPathSum(grid)
    print(res)