"""
Reverse Integer
"""


class Solution:
    def reverse(self, x: int) -> int:
        less_than_zero = False
        if x < 0:
            less_than_zero = True

        x = abs(x)
        if x == 0:
            return x

        reversed_number = 0
        while x:
            last_digit = x % 10
            x //= 10
            reversed_number = reversed_number * 10 + last_digit

        if reversed_number > 2**31 - 1:
            return 0
        return reversed_number * -1 if less_than_zero else reversed_number
