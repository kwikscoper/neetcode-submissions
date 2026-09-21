class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        charSeenAt = {}

        for right, char in enumerate(s):
            if char in charSeenAt:
                left = max(left, charSeenAt[char] + 1)            
            charSeenAt[char] = right

            res = max(res, right - left + 1)

        return res