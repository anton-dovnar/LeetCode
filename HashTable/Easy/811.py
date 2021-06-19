"""
Subdomain Visit Count
"""
from collections import deque


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_table = dict()
        for record in cpdomains:
            count, domain = record.split()
            queue = deque(domain.split("."))
            while queue:
                if domain in hash_table:
                    hash_table[domain] += int(count)
                else:
                    hash_table[domain] = int(count)
                queue.popleft()
                domain = ".".join(queue)
        return [f"{value} {key}" for key, value in hash_table.items()]
