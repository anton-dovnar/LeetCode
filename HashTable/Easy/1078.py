"""
Occurrences After Bigram
"""


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        third_words = list()
        words = text.split()
        for i in range(len(words) - 2):
            if words[i] == first:
                if words[i + 1] == second:
                    third_words.append(words[i+2])
        return third_words
