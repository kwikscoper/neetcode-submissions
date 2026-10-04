class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digitToLetter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        #for each digit, select one of the letters
        output = []
        def backtrack(digit_idx, substring):
            if digit_idx >= len(digits):
                output.append(substring)
                return

            for char in digitToLetter[digits[digit_idx]]:
                backtrack(digit_idx + 1, substring + char)

        backtrack(0, "")
        return output