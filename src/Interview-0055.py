#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归后续遍历，每一个节点的深度 = 其子节点中最大深度 + 1
# 另解: 层序遍历
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

if __name__ == '__main__':
    import utils
    nodes = [3, 9, 20, None, None, 15, 7]
    root = utils.gen_btree(nodes, 0)
    
    res = Solution().maxDepth(root)
    print(res)