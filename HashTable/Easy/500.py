"""
Keyboard Row
"""


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_row = []
        for word in words:
            word_lower = word.lower()
            if set(word_lower) == set(word_lower) & set("qwertyuiop"):
                keyboard_row.append(word)
            elif set(word_lower) == set(word_lower) & set("asdfghjkl"):
                keyboard_row.append(word)
            elif set(word_lower) == set(word_lower) & set("zxcvbnm"):
                keyboard_row.append(word)
        return keyboard_row
