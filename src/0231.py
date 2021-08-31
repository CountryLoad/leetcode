#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 进化思路：2的整数幂要自然联想位运算


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        max_power = 32
        tmp = 1
        while max_power > 0:
            if tmp == n:
                return True
            elif tmp > n:
                return False
            else:
                tmp = tmp * 2
            max_power -= 1

    def isPowerOfTwoBetter(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    test = {1: True, 2: True, 3: False, 4: True, 5: False}
    s = Solution()
    for i in test.keys():
        assert test.get(i) == s.isPowerOfTwo(i)
        assert test.get(i) == s.isPowerOfTwoBetter(i)