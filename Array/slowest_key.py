class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_pressed = releaseTimes[0], 0
        for i in range(len(releaseTimes)-1):
            dur = releaseTimes[i+1] - releaseTimes[i] 
            if dur == longest_pressed[0]:
                key = longest_pressed[1] if keysPressed[longest_pressed[1]] > keysPressed[i+1] else i+1
                longest_pressed = dur, key
            elif dur > longest_pressed[0]:
                longest_pressed = dur, i+1
        return keysPressed[longest_pressed[1]]
