class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hashtable = {}

        for n in arr:
            if n not in hashtable:
                hashtable[n] = 1
            else:
                hashtable[n] += 1

        for n in target:
            if n not in hashtable or hashtable[n] == 0:
                return False
            else:
                hashtable[n] -= 1
        return True
