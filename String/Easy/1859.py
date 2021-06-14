"""
Sorting the Sentence
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split()
        result = [0] * len(word_list)
        for word in word_list:
            result[int(word[-1]) - 1] = word[:-1]
        return " ".join(result)
