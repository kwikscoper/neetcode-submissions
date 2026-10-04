class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        sol = []
        used = [False] * len(nums)
        def dfs():
            if len(sol) == len(nums):
                output.append(sol[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue

                sol.append(nums[i])
                used[i] = True
                dfs()
                used[i] = False
                sol.pop()

        dfs()
        return output