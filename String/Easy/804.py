"""
Unique MOrse Code Words
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."] 
        result = set()
        for word in words:
            temp = ""
            for letter in word:
                temp += morse[ord(letter) - 97]
            result.add(temp)
        return len(result)
