"""
Goat Latin
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0] in vowels:
                sentence[i] = sentence[i] + "ma" + "a" * (i+1)
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + "ma" + "a" * (i+1)
        return " ".join(sentence)
