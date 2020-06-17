#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 层序遍历，子节点存储应用队列，先进先出，偷懒用list，然后顺序遍历
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        root_list = [root]
        children = []
        while root_list:
            res.append([n.val for n in root_list])
            for n in root_list:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            root_list = children
            children = []
        return res

if __name__ == '__main__':
    import utils
    nodes = [3, 9, 20, None, None, 15, 7]
    root = utils.gen_btree(nodes, 0)
    
    res = Solution().levelOrder(root)
    print(res)