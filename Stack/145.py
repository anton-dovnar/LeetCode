"""
Binary Tree Postorder Traversal

Runtime: 32 ms, faster than 59.92% of Python3 online submissions
for Binary Tree Postorder Traversal.
Memory Usage: 14.3 MB, less than 44.70% of Python3 online submissions
for Binary Tree Postorder Traversal.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        if root:
            stack.extend(self.postorderTraversal(root.left))
            stack.extend(self.postorderTraversal(root.right))
            stack.append(root.val)
        return stack
