#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 543. 二叉树的直径


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0

        def helper(node):
            if node is None:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            diameter = left + right
            if diameter > self.max_diameter:
                self.max_diameter = diameter

            return max(left, right) + 1

        helper(root)
        return self.max_diameter



if __name__ == '__main__':
    import utils
    nodes = [1, 2, 3, 4, 5, None, None]
    # nodes = [1, 2, 3, 4, 5, None, None, 6, 7, 8, 9]
    root = utils.gen_btree(nodes, 0)
    res = Solution().diameterOfBinaryTree(root)
    print (res)