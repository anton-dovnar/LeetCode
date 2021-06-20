"""
Longest Palindrome
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest_palindrome = 0
        for value in Counter(s).values():
            longest_palindrome += value // 2 * 2
            if longest_palindrome % 2 == 0 and value % 2 == 1:
                longest_palindrome += 1
        return longest_palindrome
