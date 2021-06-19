"""
Buddy Strings
"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True

        letters = list(s)
        swap_indexes = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                swap_indexes.append(i)

        if len(swap_indexes) != 2:
            return False
        else:
            letters[swap_indexes[0]], letters[swap_indexes[1]] = letters[swap_indexes[1]], letters[swap_indexes[0]]

        return ''.join(letters) == goal
