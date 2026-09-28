class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for col in range(len(board)):
                cellVal = board[row][col]
                if cellVal == '.':
                    continue
                if cellVal in seen:
                    return False
                
                seen.add(cellVal)

        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                cellVal = board[row][col]
                if cellVal == '.':
                    continue
                if cellVal in seen:
                    return False
                
                seen.add(cellVal)

        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j
                    cellVal = board[row][col]
                    if cellVal == '.':
                        continue
                    if cellVal in seen:
                        return False

                    seen.add(cellVal)

        return True