"""
Shuffle String
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ""
        for _, letter in sorted(zip(indices, s)):
            result += letter
        return result
