class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        output = []
        def backtrack(i):
            if i >= len(nums):
                output.append(sol[:])
                return

            #use value at this index
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            #dont ever use the value at this index even if you see it again
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[i]: 
                j += 1
            backtrack(j + 1)

        backtrack(0)
        return list(output)