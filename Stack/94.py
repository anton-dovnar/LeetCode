"""
Binary Tree Inorder Traversal

Runtime: 32 ms, faster than 59.88% of Python3 online submissions
for Binary Tree Inorder Traversal.
Memory Usage: 14.1 MB, less than 74.36% of Python3 online submissions
for Binary Tree Inorder Traversal.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        if root:
            stack.extend(self.inorderTraversal(root.left))
            stack.append(root.val)
            stack.extend(self.inorderTraversal(root.right))
        return stack
