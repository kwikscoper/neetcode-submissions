class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: #if mid element > right element, smallest on the right
                left = mid + 1
            else:
                right = mid

        pivot = left

        if nums[pivot] <= target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1