"""
Maximum Score After Splitting a String
"""


class Solution:
    def maxScore(self, s: str) -> int:
        zeros = ones = 0
        maximum_score = float("-inf")

        for i in range(len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            maximum_score = max(maximum_score, zeros + ones)

        return maximum_score - ones + (1 if s[-1] == "1" else 0)
