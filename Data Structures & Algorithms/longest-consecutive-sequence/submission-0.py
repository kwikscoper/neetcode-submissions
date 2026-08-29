class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxlen = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                currlen = 0
                while num in numsSet:
                    currlen += 1
                    num += 1
                
                maxlen = max(maxlen, currlen)

        return maxlen