#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 343. 整数拆分
# https://leetcode-cn.com/problems/integer-break/
# 思路：数学方法，
# 拆分规则：
# 最优： 3 。把数字 n 可能拆为多个因子 3 ，余数可能为 0,1,2 三种情况。
# 次优： 2 。若余数为 2 ；则保留，不再拆为 1+1 。
# 最差： 1 。若余数为 1 ；则应把一份 3 + 1 替换为 2 + 2，因为 2 × 2 > 3 ×1。


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = {2: 1, 3: 2, 4: 4}
        if n in base.keys():
            return base[n]

        factors = []
        while n > 4:
            factors.append(3)
            n -= 3
        res = n
        for i in factors:
            res *= i
        return res


if __name__ == "__main__":
    n = 10
    res = Solution().integerBreak(n)
    print(res)
