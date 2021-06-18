"""
Valid Palindrome II
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                delete_left_char = s[left+1:right+1]
                delete_right_char = s[left:right]
                return delete_left_char == delete_left_char[::-1] or delete_right_char == delete_right_char[::-1]
            left += 1
            right -= 1
        return True

