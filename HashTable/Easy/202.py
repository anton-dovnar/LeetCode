"""
Happy Number
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        squared_sum = 0
        while n > 1:
            to_square = n
            while to_square:
                squared_sum += (to_square % 10) ** 2
                to_square //= 10
            n = squared_sum
            squared_sum = 0
            if n in seen:
                return False
            seen.add(n)
        return n
