"""
Word Pattern
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False

        hash_map = dict()
        for letter, word in zip(pattern, s):
            if letter in hash_map:
                if hash_map[letter] != word:
                    return False
            else:
                if word in hash_map.values():
                    return False
                hash_map[letter] = word
        return True
