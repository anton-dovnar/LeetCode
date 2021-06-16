"""
Reformat Phone Number
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        result = []

        i = 0
        while i < len(number):
            if len(number[i:]) > 4:
                result.append(number[i:i+3])
                i += 3
            elif len(number[i:]) == 4:
                result.append(number[i:][:2])
                result.append(number[i:][2:4])
                break
            elif len(number[i:]) == 3:
                result.append(number[i:])
                break
            else:
                result.append(number[i:][:2])
                break
        return "-".join(result)
