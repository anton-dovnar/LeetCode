"""
Isomorphic Strings
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = dict()
        for char_s, char_t in zip(s, t):
            if char_t not in hash_map:
                if char_s in hash_map.values():
                    return False
                hash_map[char_t] = char_s
            elif hash_map[char_t] != char_s:
                return False
        return True
