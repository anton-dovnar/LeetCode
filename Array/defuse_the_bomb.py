class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for _ in range(len(code))]
        result = []
        for i in range(len(code)):
            if k > 0:
                x = len(code[i+1:i+1+k])
                if x < k:
                    result.append(sum(code[i+1:i+1+k]) + sum(code[:k-x]))
                else:
                    result.append(sum(code[i+1:i+1+k]))
            if k < 0:
                x = len(code[i+k:i])
                if x == 0:
                    result.append(sum(code[:i]) + sum(code[i+k:]))
                else:
                    result.append(sum(code[i+k:i]))
        return result
