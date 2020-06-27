#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 530. Minimum Absolute Difference in BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中序遍历解决二叉搜索树问题，不要忘记浮点数最大值 float("inf")
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pre = float("inf")
        self.min_diff = float("inf")

        def helper(root):
            if not root:
                return root
            
            helper(root.left)
            self.min_diff = min(self.min_diff, abs(root.val - self.pre))
            self.pre = root.val
            helper(root.right)
        helper(root)

        return self.min_diff

if __name__ == '__main__':
    import utils
    nodes = [0, None, 2236, 1277, 2776, 519]
    root = utils.gen_btree(nodes, 0)

    res = Solution().getMinimumDifference(root)
    print(res)