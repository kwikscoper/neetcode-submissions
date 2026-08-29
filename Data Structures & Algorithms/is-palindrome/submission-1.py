class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for char in s:
            if char.isalnum():
                string.append(char.lower())

        string = "".join(string)
        return string == string[::-1]