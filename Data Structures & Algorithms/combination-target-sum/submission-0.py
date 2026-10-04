class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # for each number as we go through the list, either choose the number
        # and run again on the same item or don't and go to the next item
        # stop if sum == target (in which case we add to result)
        # or sum > target or we hit the end of the list

        output = []
        subset = []
        def dfs(i, subsetSum):
            if subsetSum == target:
                output.append(subset[:])
                return
            if subsetSum > target or i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i, subsetSum + nums[i]) #go with same number

            subset.pop()
            dfs(i + 1, subsetSum) #skip number and go next

        dfs(0, 0)
        return output