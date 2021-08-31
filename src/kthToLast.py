#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 思路：快慢指针


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        slow = head
        fast = head

        while k > 0:
            if fast is not None:
                fast = fast.next
            k = k - 1

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow.val