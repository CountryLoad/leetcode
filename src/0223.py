#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 223. 矩形面积
# https://leetcode-cn.com/problems/rectangle-area/


class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        s1 = (ax2 - ax1) * (ay2 - ay1)
        s2 = (bx2 - bx1) * (by2 - by1)
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        height = max(top - bottom, 0)
        width = max(right - left, 0)
        return s1 + s2 - height * width


if __name__ == "__main__":
    # ax1 = -3
    # ay1 = 0
    # ax2 = 3
    # ay2 = 4
    # bx1 = 0
    # by1 = -1
    # bx2 = 9
    # by2 = 2

    ax1 = -2
    ay1 = -2
    ax2 = 2
    ay2 = 2
    bx1 = -2
    by1 = -2
    bx2 = 2
    by2 = 2

    res = Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    print(res)
