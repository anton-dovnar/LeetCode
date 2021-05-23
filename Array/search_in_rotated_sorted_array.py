class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        return self.find_key(nums, start, end, target)

    def find_key(self, arr: List[int], start: int, end: int, key: int) -> int:
        if start > end:
            return -1

        mid = (start + end) // 2
        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid]:
            if arr[start] <= key <= arr[mid]:
                return self.find_key(arr, start, mid - 1, key)
            return self.find_key(arr, mid + 1, end, key)

        if arr[mid] <= key <= arr[end]:
            return self.find_key(arr, mid + 1, end, key)
        return self.find_key(arr, start, mid - 1, key)
