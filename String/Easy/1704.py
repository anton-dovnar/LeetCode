"""
Determine if String Halves Are Alike
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        half = len(s) // 2
        first_half = s[half:]
        second_half = s[:half]
        first_half_counter = 0
        second_half_counter = 0

        for vowel in "aeiou":
            first_half_counter += first_half.count(vowel)
            second_half_counter += second_half.count(vowel)

        return first_half_counter == second_half_counter
