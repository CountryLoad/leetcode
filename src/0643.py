#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 643. 子数组最大平均数 I
# https://leetcode-cn.com/problems/maximum-average-subarray-i/
# 思路：滑动窗口



class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = sum_tmp = sum(nums[:k])

        for i in range(k, len(nums)):
            sum_tmp = sum_tmp + nums[i] - nums[i - k]
            max_sum = max(max_sum, sum_tmp)

        return float(max_sum) / k


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    res = Solution().findMaxAverage(nums, k)
    print(res)