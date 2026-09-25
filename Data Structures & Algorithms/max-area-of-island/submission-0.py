class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(row, col):
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            up = down = left = right = 0
            if row > 0:
                up = dfs(row - 1, col)
            if col > 0:
                left = dfs(row, col - 1)
            if row < rows - 1:
                down = dfs(row + 1, col)
            if col < cols - 1:
                right = dfs(row, col + 1)

            return 1 + up + left + down + right
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))

        return maxArea