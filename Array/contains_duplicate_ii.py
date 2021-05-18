class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, n in enumerate(nums):
            if n in hashmap:
                for j in hashmap[n]:
                    if abs(i - j)  <= k:
                        return True
                hashmap[n].append(i)
            else:
                hashmap[n] = [i]
        return False
