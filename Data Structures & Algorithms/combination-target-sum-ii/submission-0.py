class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #for each number in candidates, either choose it or skip it
        candidates.sort()
        output = []
        def backtrack(candidate_idx, curr_sol, curr_sum):
            if curr_sum == target:
                output.append(curr_sol)
                return
            if curr_sum > target or candidate_idx >= len(candidates):
                return

            candidate = candidates[candidate_idx]
            backtrack(candidate_idx + 1, curr_sol + [candidate], curr_sum + candidate)
            
            j = candidate_idx
            while j < len(candidates) and candidates[j] == candidates[candidate_idx]:
                j += 1
            backtrack(j, curr_sol, curr_sum)

        backtrack(0, [], 0)
        return output