class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def fill(row, col):
            if image[row][col] != start_color:
                return

            image[row][col] = color

            if row > 0: fill(row - 1, col)
            if col > 0: fill(row, col - 1)
            if row + 1 < rows: fill(row + 1, col)
            if col + 1 < cols: fill(row, col + 1)

            return

        fill(sr, sc)

        return image