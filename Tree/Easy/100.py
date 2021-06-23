"""
Same Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = []
        while stack or p or q:
            if p and not q or q and not p:
                return False
            elif p and q:
                if p.val == q.val:
                    stack.extend([p, q])
                    p = p.left
                    q = q.left
                else:
                    return False
            else:
                q = stack.pop()
                p = stack.pop()
                q = q.right
                p = p.right
        return True
