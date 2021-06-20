"""
Minimum Index Sum of Two Lists
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_table = {value: key for key, value in enumerate(list1)}
        best, longest_interest = float('inf'), []
        for key, value in enumerate(list2):
            i = hash_table.get(value, float('inf'))
            if i + key < best:
                best = i + key
                longest_interest = [value]
            elif i + key == best:
                longest_interest.append(value)
        return longest_interest
