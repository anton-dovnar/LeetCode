"""
Range Sum of BST
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        count = 0

        if root.val and low <= root.val <= high:
            count += root.val
        if root.left:
            count += self.rangeSumBST(root.left, low, high)
        if root.right:
            count += self.rangeSumBST(root.right, low,  high)

        return count
