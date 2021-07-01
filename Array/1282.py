"""
Group the People Given the Group Size The Belong To
"""

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = dict.fromkeys(groupSizes)

        for key, value in enumerate(groupSizes):
            if hashmap[value]:
                hashmap[value].append(key)
            else:
                hashmap[value] = [key]

        result = []
        for key, value in hashmap.items():
            for i in range(0, len(hashmap[key]), key):
                result.append(hashmap[key][i:i+key])
        return result
