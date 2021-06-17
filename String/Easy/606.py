"""
Construct String from Binary Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""

        string_from_binary_tree = str(root.val)
        if root.left:
            string_from_binary_tree += f"({self.tree2str(root.left)})"
        if not root.left and root.right:
            string_from_binary_tree += "()"
        if root.right:
            string_from_binary_tree += f"({self.tree2str(root.right)})"
        return string_from_binary_tree
