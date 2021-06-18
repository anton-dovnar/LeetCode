"""
Most Common Word
"""
import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^a-zA-Z ]', " ", paragraph)
        banned = set(banned)
        word_appearances = Counter(paragraph.split())
        for word in word_appearances.most_common():
            if word[0] not in banned:
                return word[0]
