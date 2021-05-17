from itertools import combinations

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = [sorted(d) for d in dominoes]
        hashmap = {}
        print(dominoes)
        for domino in dominoes:
            a, b = domino
            if (a, b) in hashmap:
                hashmap[(a,b)] = hashmap[(a,b)] + 1 if hashmap[(a,b)] else hashmap[(a,b)] + 2
            else:
                hashmap[(a,b)] = 0
        counter = 0
        for k in hashmap:
            counter += len(list(combinations([i for i in range(hashmap[k])], 2)))
        return counter
