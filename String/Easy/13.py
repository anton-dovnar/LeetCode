"""
Roman to Integer
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        value = 0
        for i in range(len(s)):
            if i > 0 and roman_table[s[i]] > roman_table[s[i-1]]:
                value += roman_table[s[i]] - 2 * roman_table[s[i-1]]
            else:
                value += roman_table[s[i]]
        return value
