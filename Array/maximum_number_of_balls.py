class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        for i in range(lowLimit, highLimit + 1):
            box_number = 0
            while i:
                box_number += i % 10
                i //= 10
            if box_number in boxes:
                boxes[box_number] += 1
            else:
                boxes[box_number] = 1
        return max(boxes.values())
