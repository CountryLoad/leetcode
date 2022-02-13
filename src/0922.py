#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 922. 按奇偶排序数组 II
# https://leetcode-cn.com/problems/sort-array-by-parity-ii/
# 思路： a 原数组可更改：双指针
# b 原数组不可更改：两次遍历

class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        index = 0
        for i in nums:
            if i % 2 == 0:
                res[index] = i
                index += 2
        index = 1
        for i in nums:
            if i % 2 != 0:
                res[index] = i
                index += 2
        return res

    def sortArrayByParityII_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j, n = 0, 1, len(nums)

        while i < n:
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 2
            else:
                i += 2

        return nums


if __name__ == '__main__':
    nums = [4, 2, 5, 7]
    res = Solution().sortArrayByParityII(nums)

    res1 = Solution().sortArrayByParityII_1(nums)
    print(res)
    print(res1)
