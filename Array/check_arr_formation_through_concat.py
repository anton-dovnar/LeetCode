class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if len(pieces) == 1 and pieces[0] != arr:
            return False
        temp = set(arr)
        for row in pieces:
            for i in range(len(row)-1):
                if row[i] not in temp:
                    return False
                else:
                    idx = arr.index(row[i])
                if (next_el := row[i+1]):
                    try:
                        if next_el != arr[idx+1]:
                            return False
                    except:
                        return False
        return True
