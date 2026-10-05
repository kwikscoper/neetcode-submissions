class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        memo = [[None] * cols for row in range(rows)]

        def dfs(row, col):
            if row == rows - 1 and col == cols - 1:
                return 1
            if row >= rows or col >= cols:
                return 0
            if memo[row][col] is not None:
                return memo[row][col]

            right = dfs(row, col + 1)
            down = dfs(row + 1, col)

            memo[row][col] = right + down
            return memo[row][col]

        return dfs(0, 0)