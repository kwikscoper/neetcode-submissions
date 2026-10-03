class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        output = 0

        left = 0
        for right, char in enumerate(s):
            counts[char] += 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            output = max(output, right - left + 1)

        return output