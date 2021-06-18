"""
Ransom Note
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = Counter(ransomNote)
        magazine_map = Counter(magazine)
        ransom_map.subtract(magazine_map)
        for value in ransom_map.values():
            if value > 0:
                return False
        return True
