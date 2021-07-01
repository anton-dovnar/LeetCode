class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if not s and not goal:
            return True
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False
