#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 283. Move Zeroes

# 双指针.另一简单解法，两次遍历，只要把数组中所有的非零元素，按顺序给数组的前段元素位赋值，剩下的全部直接赋值 0，非最优
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tail = 0
        for i in range(len(nums)):
            head = i
            if nums[head] != 0:
                nums[head], nums[tail] = nums[tail], nums[head]
                tail = tail + 1

        return nums


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]

    res = Solution().moveZeroes(nums)
    print(res)
