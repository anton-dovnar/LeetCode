class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        length = len(startTime)
        if length == 1 and startTime[0] == queryTime:
            return 1

        counter = 0
        for i in range(length):
            if queryTime in list(range(startTime[i], endTime[i] + 1)):
                counter += 1
        return counter
