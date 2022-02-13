#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 387. 字符串中的第一个唯一字符
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)

        for idx, c in enumerate(s):
            if count[c] == 1:
                return idx
        return -1


if __name__ == '__main__':
    s = "loveleetcode"
    res = Solution().firstUniqChar(s)
    print(res)