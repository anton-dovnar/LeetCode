"""
Delete Columns to Make Sorted
"""


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns_to_delete = 0
        for column in list(zip(*strs)):
            frontier = column[0]
            for letter in column[1:]:
                if letter < frontier:
                    columns_to_delete += 1
                    break
                frontier = letter
        return columns_to_delete
