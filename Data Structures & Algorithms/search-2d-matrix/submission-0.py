class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        row = lambda coord: coord // len(matrix[0])
        col = lambda coord: coord % len(matrix[0])

        while left <= right:
            mid = ((right - left) // 2) + left
            if matrix[row(mid)][col(mid)] < target:
                left = mid + 1
            elif matrix[row(mid)][col(mid)] > target:
                right = mid - 1
            else:
                return True
        
        return False