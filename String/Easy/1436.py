"""
Destination City
"""
from collections import Counter


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash_map = Counter(sum(paths, []))
        for path_a, path_b in paths:
            if hash_map[path_b] == 1:
                return path_b
