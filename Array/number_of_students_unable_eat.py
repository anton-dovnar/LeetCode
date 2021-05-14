from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        a = len(students)
        b = len(sandwiches)
        i = 0
        students = deque(students)
        swaps = 0
        while a or b:
            if swaps == len(students):
                break
            if students[i] == sandwiches[i]:
                swaps = 0
                students.popleft()
                sandwiches.pop(i)
                a -= 1
                b -= 1
            else:
                swaps += 1
                el = students.popleft()
                students.append(el)
        return a
