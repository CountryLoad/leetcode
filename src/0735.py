#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 思路 栈
# 735. 行星碰撞
# https://leetcode-cn.com/problems/asteroid-collision/
# 官方的解法，巧妙用 while else，优秀

# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         ans = []
#         for new in asteroids:
#             while ans and new < 0 < ans[-1]:
#                 if ans[-1] < -new:
#                     ans.pop()
#                     continue
#                 elif ans[-1] == -new:
#                     ans.pop()
#                 break
#             else:
#                 ans.append(new)
#         return ans


# 有些冗余代码，如，a明确小于0，用-a就好，不用abs(a)
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        def crush(s, a):
            if not stack:
                s.append(a)
                return s
            if s[-1] < 0:
                s.append(a)
                return s
            elif s[-1] > 0:
                if abs(s[-1]) > abs(a):
                    return s
                elif abs(s[-1]) == abs(a):
                    s.pop()
                    return s
                else:
                    s.pop()
                    return crush(s, a)

        stack = []
        for i in asteroids:
            if stack and i < 0:
                stack = crush(stack, i)
            else:
                stack.append(i)

        return stack


if __name__ == '__main__':
    # asteroids = [5, 10, -5]
    # asteroids = [8, -8]
    # asteroids = [10, 2, -5]
    asteroids = [-2, -1, 1, 2]
    # asteroids = [1, -2, -2, -2]

    print(Solution().asteroidCollision(asteroids))
