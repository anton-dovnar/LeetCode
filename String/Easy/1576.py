"""
Replace All ?'s to Avoid Consecutive Repeating Characters
"""
from string import ascii_lowercase


class Solution:
    def find_next_letter(self, letter):
        i = 0
        flag = True
        while flag:
            if ascii_lowercase[i] not in letter:
                match = ascii_lowercase[i]
                flag = False
            i += 1
        return match

    def modifyString(self, s: str) -> str:
        if len(s) == 1:
            return "a"
        letters = list(s)
        for i in range(len(letters)):
            if letters[i] == '?':
                if i == 0:
                    letters[i] = self.find_next_letter(letters[i+1])
                elif i == len(letters) - 1:
                    letters[i] = self.find_next_letter(letters[i-1])
                else:
                    letters[i] = self.find_next_letter(letters[i-1] + letters[i+1])

        return "".join(letters)
