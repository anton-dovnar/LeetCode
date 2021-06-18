"""
Latest Time by Replacing Hidden Digits
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        valid_table = {
            0: '2',
            1: '9',
            3: '5',
            4: '9'
        }
        time = list(time)
        for i in range(len(time)):
            if time[i] == "?":
                if i == 1 and time[i-1] == "2":
                    time[i] = '3'
                elif i == 0 and time[i+1] > '3' and time[i+1] != '?':
                    time[i] = '1'
                else:
                    time[i] = valid_table[i]
        return "".join(time)
