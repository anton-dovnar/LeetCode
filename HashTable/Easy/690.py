"""
Employee Importance
"""
from collections import deque
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hash_table = dict()
        for employee in employees:
            hash_table[employee.id] = (employee.importance, employee.subordinates)

        total_importance = hash_table[id][0]
        subordinates = deque(hash_table[id][1])
        #BFS NA MINIMALKAH
        while subordinates:
            subordinate = subordinates[0]
            total_importance += hash_table[subordinate][0]
            if hash_table[subordinate][1]:
                subordinates.extend(hash_table[subordinate][1])
            subordinates.popleft()

        return total_importance
