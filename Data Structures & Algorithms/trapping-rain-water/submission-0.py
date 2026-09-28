class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                totalWater += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                totalWater += rightMax - height[right]
                right -= 1

        return totalWater

        #start total water at zero
        #initialize left and right pointers
        #leftMax is highest wall seen by left, rightMax is highest wall seen by right
        #if leftMax < rightMax:
            #add leftMax - currHeight to total water
            #move left pointer in

        #same for right

        #return totalWater