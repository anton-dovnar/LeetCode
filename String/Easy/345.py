"""
Reverse Vowels of a String
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        sequence = list(s)
        vowels = [character for character in s if character in "aeiouAEIOU"][::-1]
        i = 0
        for j in range(len(sequence)):
            if sequence[j] in "aeiouAEIOU":
                sequence[j] = vowels[i]
                i += 1
        return "".join(sequence)
