class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums = [str(n) for n in num]
        return list(str(int(''.join(nums)) + k))
