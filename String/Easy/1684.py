"""
Count the Number of Consistent Strings
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        allowed = set(allowed)
        for word in words:
            consistent = True
            for char in word:
                if char not in allowed:
                    consistent = False
                    break

            if consistent:
                counter += 1

        return counter
