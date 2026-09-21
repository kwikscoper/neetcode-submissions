class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                count = 1
                while num + 1 in numsSet:
                    num += 1
                    count += 1

                res = max(res, count)

        return res