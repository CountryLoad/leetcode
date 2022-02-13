#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1122. 数组的相对排序
# https://leetcode-cn.com/problems/relative-sort-array/
# 思路：计数排序

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # 可用 collections.Counter
        # count = collections.Counter(arr1)
        count = dict()
        for i in arr1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        res = []
        for i in arr2:
            while count.get(i) > 0:
                res.append(i)
                count[i] -= 1

        tmp = []
        for k in count:
            while count[k] > 0:
                tmp.append(k)
                count[k] -= 1
        tmp = sorted(tmp)

        res += tmp
        return res


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    # res = [2,2,2,1,4,3,3,9,6,7,19]
    res = Solution().relativeSortArray(arr1, arr2)
    print(res)
