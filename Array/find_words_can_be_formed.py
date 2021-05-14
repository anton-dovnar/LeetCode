class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        for word in words:
            flag = True
            for c in word:
                if not 0 < word.count(c) <= chars.count(c):
                    flag = False
                    break
            if flag:
                output += len(word)
        return output
