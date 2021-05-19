class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        for j, v in enumerate(rating):
            left_side_less = 0
            left_side_greater = 0
            right_side_less = 0
            right_side_greater = 0
            for i in rating[:j]:
                if i < v:
                    left_side_less += 1
                else:
                    left_side_greater += 1
            for k in rating[j+1:]:
                if k < v:
                    right_side_less += 1
                else:
                    right_side_greater += 1
            counter += left_side_less * right_side_greater + left_side_greater * right_side_less
        return counter
