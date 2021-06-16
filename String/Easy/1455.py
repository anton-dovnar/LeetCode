"""
Check If a Word Occurs As a Prefix of Any Word in Sentence
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for index, word in enumerate(sentence.split()):
            if word[:len(searchWord)] == searchWord:
                return index + 1
        return -1
