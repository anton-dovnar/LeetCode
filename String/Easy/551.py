"""
Student Attendance Record I
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        consecutive_late = 0
        for character in s:
            if character == 'A':
                absent += 1
                consecutive_late = 0
            elif character == 'L':
                consecutive_late += 1
                if consecutive_late == 3:
                    return False
            else:
                consecutive_late = 0
        return absent < 2
