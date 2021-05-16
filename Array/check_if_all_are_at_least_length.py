class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        seen = False
        places = 0
        for n in nums:
            if n == 1:
                if seen:
                    if places >= k:
                        places = 0
                    else:
                        return False
                else:
                    seen = True
            else:
                places += 1
        return True
