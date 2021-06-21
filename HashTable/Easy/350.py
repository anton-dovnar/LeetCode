"""
Intersection of Two Arrays II
"""
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_numbers(a, b):
            hash_b = Counter(b)
            intersection = []
            for number in a:
                validate = hash_b.get(number, 0)
                if validate:
                    intersection.append(number)
                    hash_b[number] -= 1
            return intersection

        return get_numbers(nums1, nums2) if len(nums1) < len(nums2) else get_numbers(nums2, nums1)
