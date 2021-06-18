class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        current = 0
        result = ""
        while a or b or current:
            if a:
                current += int(a.pop())
            if b:
                current += int(b.pop())

            result += str(current % 2)
            current //= 2
        return result[::-1]
