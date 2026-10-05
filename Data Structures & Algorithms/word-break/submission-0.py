class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for word in wordSet:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return memo[i]
            
            memo[i] = False
            return memo[i]

        return dfs(0)