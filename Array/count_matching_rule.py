class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys = {
            'type': 0,
            'color': 1,
            'name': 2,
        }
        counter = 0
        for obj in items:
            if obj[keys[ruleKey]] == ruleValue:
                counter += 1
        return counter
