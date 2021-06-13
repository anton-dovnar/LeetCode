"""
Binary Tree Preorder Traversal

Runtime: 32 ms, faster than 60.40% of Python3 online submissions
for Binary Tree Preorder Traversal.
Memory Usage: 14.2 MB, less than 73.22% of Python3 online submissions
for Binary Tree Preorder Traversal.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        if root:
            stack.append(root.val)
            stack.extend(self.preorderTraversal(root.left))
            stack.extend(self.preorderTraversal(root.right))
        return stack
