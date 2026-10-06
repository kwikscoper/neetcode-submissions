class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #at each step, i have the choice to either jump 1 or 2 steps
        #i must pay the cost each time

        memo = [None] * len(cost) #stores the minimum cost to reach the top from i
        def dfs(i):
            if i >= len(cost): #we are at the top of the staircase
                return 0
            if memo[i] is not None:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))