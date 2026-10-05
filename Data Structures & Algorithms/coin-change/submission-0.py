class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [None] * (amount + 1)
        def dfs(remaining):
            minCoins = float('inf')
            if remaining == 0:
                return 0
            if memo[remaining] is not None:
                return memo[remaining]

            for coin in coins:
                if coin > remaining:
                    continue
                neededCoins = 1 + dfs(remaining - coin)
                minCoins = min(minCoins, neededCoins)
            
            memo[remaining] = minCoins
            return minCoins

        output = dfs(amount)
        return output if output != float('inf') else -1