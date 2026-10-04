class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for row in range(rows)]

        def dfs(char_idx, row, col):
            if char_idx >= len(word):
                return True
            if row < 0 or col < 0 or row >= rows or col >= cols or visited[row][col]:
                return False
            if board[row][col] != word[char_idx]:
                return False
            

            next_idx = char_idx + 1
            visited[row][col] = True
            up = dfs(next_idx, row - 1, col)
            down = dfs(next_idx, row + 1, col)
            left = dfs(next_idx, row, col - 1)
            right = dfs(next_idx, row, col + 1)
            visited[row][col] = False

            return up or down or left or right

        for row in range(rows):
            for col in range(cols):
                foundWord = dfs(0, row, col)
                if foundWord:
                    return True

        return False