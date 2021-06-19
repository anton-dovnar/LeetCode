class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_table = dict()
        for element in arr:
            if element in hash_table:
                hash_table[element] += 1
            else:
                hash_table[element] = 1

        return len(set(hash_table.values())) == len(hash_table.values())
