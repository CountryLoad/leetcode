#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 226. Invert Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 套递归框架
class Solution:
    def invertTree(self, root):
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    import utils
    nodes = [4, 2, 7, 1, 3, 6, 9]
    root = utils.gen_btree(nodes, 0)

    res = Solution().invertTree(root)
    print(utils.print_btree(res))