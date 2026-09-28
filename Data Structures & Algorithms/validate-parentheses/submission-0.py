class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in bracketMap:
                if stack and stack[-1] == bracketMap[char]:
                    stack.pop()
                    continue
                else:
                    return False

            stack.append(char)

        return not stack