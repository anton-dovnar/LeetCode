"""
Maximum Number of Balloons
"""
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letter_map = Counter(text)
        counter = 0
        flag = True

        while flag:
            for letter in "balloon":
                if letter in letter_map and letter_map[letter] > 0:
                    counter += 1
                    letter_map[letter] -= 1
                else:
                    flag = False
                    break
        return counter // 7
