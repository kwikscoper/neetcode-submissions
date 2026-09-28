class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVolume = 0

        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)
            if volume > maxVolume:
                maxVolume = volume

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxVolume