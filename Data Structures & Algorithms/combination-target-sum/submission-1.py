class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #either we choose the current number or we skip and go to the next
        #add to output if currSum == target, then return
        #simply return if currSum > target or i >= len(nums)

        output = []
        def dfs(i, subset, currSum):
            if currSum == target:
                output.append(subset[:])
                return
            if currSum > target or i >= len(nums):
                return

            dfs(i, subset + [nums[i]], currSum + nums[i])
            dfs(i + 1, subset, currSum)

        dfs(0, [], 0)
        return output