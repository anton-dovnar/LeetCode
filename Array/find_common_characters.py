from collections import defaultdict

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        length = len(A)
        if length == 1:
            return A
        hashtable = defaultdict(list)
        result = []
        for word in A:
            for c in set(word):
                hashtable[c].append(word.count(c))
        for k in hashtable:
            if len(hashtable[k]) >= length:
                for _ in range(min(hashtable[k])):
                    result.append(k)
        return result
