class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(substring, numOpen, numClosed):
            if numOpen == numClosed == n:
                output.append(substring)

            if numOpen < n:
                backtrack(substring + '(', numOpen + 1, numClosed)
            if numClosed < numOpen:
                backtrack(substring + ')', numOpen, numClosed + 1)

        backtrack("", 0, 0)
        return output