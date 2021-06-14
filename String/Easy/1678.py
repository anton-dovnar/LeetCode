"""
Goal Parser Interpretation
"""


class Solution:
    def interpret(self, command: str) -> str:
        translate_table = {
            "()": "o",
            "(al)": "al"
        }
        for key in translate_table:
            command = command.replace(key, translate_table[key])
        return command
