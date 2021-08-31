
# 107. 二叉树的层序遍历 II

# 思路：程序遍历，再反转

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        cur_level = [root]
        while cur_level:
            res.append([i.val for i in cur_level])

            next_level = []
            for i in cur_level:
                if i.left is not None:
                    next_level.append(i.left)
                if i.right is not None:
                    next_level.append(i.right)
            cur_level = next_level
        return res[::-1]