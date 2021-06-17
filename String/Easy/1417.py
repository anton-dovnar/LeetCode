from itertools import zip_longest


class Solution:
    def reformat(self, s: str) -> str:
        if len(s) > 1 and (s.isalpha() or s.isdigit()):
            return ""
        letters = ""
        numbers = ""
        for character in s:
            if character.isdigit():
                numbers += character
            else:
                letters += character

        if len(numbers) >= len(letters):
           sequence = zip_longest(numbers, letters)
        else:
            sequence = zip_longest(letters, numbers)

        return ''.join(''.join(pair) if all(pair) else pair[0] for pair in sequence)
