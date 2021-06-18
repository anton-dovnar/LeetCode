class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""

        if not strs:
            return longest_prefix

        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            if all([s.startswith(shortest[:i+1]) for s in strs]):
                    longest_prefix = shortest[:i+1]
            else:
                break
        return longest_prefix
