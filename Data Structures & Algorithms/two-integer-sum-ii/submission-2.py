class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i]
            left, right = i + 1, len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] > complement:
                    right = mid - 1
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    return [i+1, mid+1]

        return []