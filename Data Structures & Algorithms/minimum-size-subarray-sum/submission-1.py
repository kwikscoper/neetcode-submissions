class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')

        windowSum = 0
        left = 0
        for right, num in enumerate(nums):
            windowSum += num
            while windowSum >= target:
                minLen = min(minLen, right - left + 1)
                windowSum -= nums[left]
                left += 1

        return minLen if minLen != float('inf') else 0