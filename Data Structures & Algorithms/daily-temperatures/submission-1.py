class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp, in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx, prevtemp = stack.pop()
                result[idx] = i - idx

            stack.append((i, temp))

        return result