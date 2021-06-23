"""
Balance Binary Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        memoization = {}
        if not root:
            return True

        def get_depth(root):
            if not root:
                return 0

            if root in memoization:
                return memoization[root]

            memoization[root] = 1 + max(get_depth(root.left), get_depth(root.right))
            return memoization[root]

        return abs(get_depth(root.left) - get_depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
