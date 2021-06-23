"""
Symmetric Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traverse(left, right):
            if not left and not right:
                return True
            if left and right:
                if left.val == right.val:
                    outer = traverse(left.left, right.right)
                    inner = traverse(left.right, right.left)
                    return outer and inner
                else:
                    return False
            else:
                return False

        if root is None:
            return True
        else:
            return traverse(root.left, root.right)
