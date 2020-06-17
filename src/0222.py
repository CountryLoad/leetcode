#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n),不算最优，没充分利用完全二叉树的特性。
# 最优：前d-1层是满二叉树(2**(d-1))-1个节点，最后一层找到最右侧节点序号即可，二分查找
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == '__main__':
    import utils
    nodes = [1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None]
    root = utils.gen_btree(nodes, 0)

    res = Solution().countNodes(root)
    print(res)