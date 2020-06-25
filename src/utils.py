#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def gen_btree(nodes, start):
    """ 生成二叉树
    nodes: 数组
    """
    if nodes[start] is None:
        return None
    root = TreeNode(nodes[start])

    lnode = 2 * start + 1
    rnode = 2 * start + 2
    if lnode < len(nodes):
        root.left = gen_btree(nodes, lnode)
    if rnode < len(nodes):
        root.right = gen_btree(nodes, rnode)
    return root


def print_btree(root):
    """ 打印二叉树，返回二叉树的数组存储形式
    """
    if not root:
        return []

    res = []
    root_list = [root]
    child_list = []
    while root_list:
        for node in root_list:
            if node:
                res.append(node.val)
            if node.left:
                child_list.append(node.left)
            if node.right:
                child_list.append(node.right)
        root_list = child_list
        child_list = []
    return res