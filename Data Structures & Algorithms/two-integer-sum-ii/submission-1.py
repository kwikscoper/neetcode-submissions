class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hmap:
                return [hmap[complement] + 1, i + 1]
            else:
                hmap[numbers[i]] = i