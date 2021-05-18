class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        temp = [0] + flowerbed + [0]
        for i in range(len(flowerbed)):
            if temp[i] == flowerbed[i] == temp[i+2] == 0:
                temp[i+1] = flowerbed[i] = 1
                n -= 1
                if not n:
                    return True
        return not n
