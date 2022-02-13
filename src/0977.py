#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 977. 有序数组的平方
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/
# 思路：双指针

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        pos = end = len(nums) -1
        res = [0] * len(nums)
        while start <= end:
            if abs(nums[start]) <= abs(nums[end]):
                res[pos] = nums[end] * nums[end]
                end -= 1
            else:
                res[pos] = nums[start] * nums[start]
                start += 1
            pos -= 1
        return res


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    res = Solution().sortedSquares(nums)
    print(res)