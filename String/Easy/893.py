"""
Groups of Special-Equivalent Strings
"""


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        return len({("".join(sorted(word[0::2])), "".join(sorted(word[1::2]))) for word in words})
