#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 26. Remove Duplicates from Sorted Array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        tail = 0

        for head in range(1, len(nums)):
            if nums[head] == nums[tail]:
                continue
            tail += 1
            nums[tail], nums[head] = nums[head], nums[tail]

        return tail + 1
        

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    count = Solution().removeDuplicates(nums)
    print(nums[:count])