#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        max_width = 0
        root_list = [(root, 0)]
        child_list = []
        while root_list:
            max_width = max(max_width, root_list[-1][1] - root_list[0][1] + 1)
            for i in range(len(root_list)):
                if root_list[i][0].left:
                    child_list.append((root_list[i][0].left, 2 * root_list[i][1] + 1))
                if root_list[i][0].right:   
                    child_list.append((root_list[i][0].right, 2 * root_list[i][1] + 2))
            root_list = child_list
            child_list = []

        return  max_width


if __name__ == '__main__':
    import utils
    # nodes = [1, 1, 1, 1, None, None, 1, 1, None, None, 1]
    nodes = [1, 3, 2, 5, 3, None, 9]
    root = utils.gen_btree(nodes, 0)

    res = Solution().widthOfBinaryTree(root)
    print(res)
