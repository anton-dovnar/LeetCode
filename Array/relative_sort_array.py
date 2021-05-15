class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashtable = {}
        for n in arr1:
            if n not in hashtable:
                hashtable[n] = 1
            else:
                hashtable[n] += 1
        result = []
        for n in arr2:
            for _ in range(hashtable[n]):
                result.append(n)
                arr1.remove(n)
        return result + sorted(arr1)
