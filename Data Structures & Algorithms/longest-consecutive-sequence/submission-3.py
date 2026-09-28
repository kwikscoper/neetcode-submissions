class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if num - 1 in numsSet:
                continue

            count = 0
            while num in numsSet:
                count += 1
                num += 1

            longest = max(longest, count)

        return longest