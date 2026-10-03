class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSeenAt = {}
        maxLen = 0

        left = 0
        for right, char in enumerate(s):
            if char in charSeenAt:
                left = max(left, charSeenAt[char] + 1)
            charSeenAt[char] = right
            maxLen = max(maxLen, right - left + 1)

        return maxLen