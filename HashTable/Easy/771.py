"""
Jewels and Stones
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_table = dict()
        for letter in stones:
            if letter in jewels:
                if letter in hash_table:
                    hash_table[letter] += 1
                else:
                    hash_table[letter] = 1
        return sum(hash_table.values())
