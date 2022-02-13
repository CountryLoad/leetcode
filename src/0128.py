#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 128. 最长连续序列
# https://leetcode-cn.com/problems/longest-consecutive-sequence/
# 时间复杂度要求为 O(n)

# 思路：利用hash，尽可能的多记录信息


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_set = set(nums)
        max_length = 1
        for i in nums:
            cur_length = 1
            if i - 1 in nums_set:
                continue

            i_tmp = i
            while i_tmp < i + len(nums_set):
                if i_tmp + 1 in nums_set:
                    i_tmp += 1
                    cur_length += 1
                else:
                    break

            max_length = max(max_length, cur_length)

        return max_length