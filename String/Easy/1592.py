"""
Rearrange Spaces Between Words
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        if spaces == 0:
            return text

        list_of_words = text.split()
        if len(list_of_words) == 1:
            return f"{list_of_words[0]}" + " " * spaces

        K = spaces // (len(list_of_words) - 1)
        result = (" " * K).join(list_of_words)
        space_reminder = spaces % (len(list_of_words) - 1)
        return result + " " * space_reminder
