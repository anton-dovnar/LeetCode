class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniq = sorted(list(set(arr)))
        ranks = zip(uniq, [i for i in range(1, len(uniq)+1)])
        hashmap = {v:r for v, r in ranks}
        return [hashmap[n] for n in arr]
