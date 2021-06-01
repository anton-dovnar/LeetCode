class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            left_val = nums[left]
            right_val = nums[right]
            mid_val = nums[mid]

            if mid_val == target:
                return True

            if mid_val < right_val:
                if mid_val < target <= right_val:
                    left = mid + 1
                else:
                    right = mid - 1
            elif mid_val > right_val:
                if left_val <= target < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1

        return nums[left] == target
