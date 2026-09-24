class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numIslands = 0

        def dfs(row, col):
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            if row > 0: dfs(row - 1, col)
            if col > 0: dfs(row, col - 1)
            if row < rows - 1: dfs(row + 1, col)
            if col < cols - 1: dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    numIslands += 1

        return numIslands
                