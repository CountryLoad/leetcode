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
