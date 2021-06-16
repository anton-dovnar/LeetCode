"""
String Matching in an Array
"""


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return list({word for index, word in enumerate(words) for obj in words[:index] + words[index+1:] if word in obj})
