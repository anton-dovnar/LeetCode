"""
Reorder Data in Log Files
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = list()
        digits = list()

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])
        return letters + digits
