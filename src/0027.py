#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 27. Remove Element

# 双指针.同 0283
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tail = 0
        for i in range(len(nums)):
            head = i
            if nums[head] != val:
                nums[head], nums[tail] = nums[tail], nums[head]
                tail = tail + 1
        return tail


if __name__ == '__main__':
    nums = [3, 2, 2, 3]  
    val = 3
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2

    tail = Solution().removeElement(nums, val)
    print(nums[:tail])
