class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        for char in s:
            if char.isalnum():
                cleanStr += char.lower()

        return cleanStr == cleanStr[::-1]