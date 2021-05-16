class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        alice_set = set(aliceSizes)
        for b in set(bobSizes):
            if diff + b in alice_set:
                return diff + b, b
