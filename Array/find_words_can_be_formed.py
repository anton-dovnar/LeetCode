class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        for word in words:
            if all([True if 0 < word.count(c) <= chars.count(c) else False for c in word]):
                output += len(word)
        return output
