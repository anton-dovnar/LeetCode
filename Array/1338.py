"""
Reduce Array Size to The Half
"""
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if len(set(arr)) == 1:
            return 1

        length = len(arr)
        count = Counter(arr)
        occurrences = sorted(count.values(), reverse=True)

        size = counter = i = 0
        while counter < length // 2:
            counter += occurrences[i]
            size += 1
            i += 1
        return size
