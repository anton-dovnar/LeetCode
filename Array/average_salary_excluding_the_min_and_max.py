class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = min(salary)
        max_sal = max(salary)
        total = 0
        employees = 0
        for i in salary:
            if i not in {min_sal, max_sal}:
                total += i
                employees += 1
        return total / employees
