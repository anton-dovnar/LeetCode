"""
Backspace String Compare

Runtime: 32 ms, faster than 62.94% of Python3 online submissions
for Backspace String Compare.
Memory Usage: 14.4 MB, less than 17.75% of Python3 online submissions
for Backspace String Compare.
"""


from itertools import zip_longest

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_letter(word):
            skip = 0
            for letter in word[::-1]:
                if letter == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield letter

        return all(x == y for x, y in zip_longest(get_letter(s), get_letter(t)))
