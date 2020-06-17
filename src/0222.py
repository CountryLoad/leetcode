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
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    res = Solution().countNodes(node1)
    print(res)
