"""
Word Pattern
"""


class solution:
    def wordpattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return false

        hash_map = dict()
        for letter, word in zip(pattern, s):
            if letter in hash_map:
                if hash_map[letter] != word:
                    return false
            else:
                if word in hash_map.values():
                    return false
                hash_map[letter] = word
        return true
