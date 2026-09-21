class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixArr = {0: 1}
        currSum = 0

        res = 0

        for num in nums:
            currSum += num
            diff = currSum - k #if this val is in prefixArr, then a subarray of sum k exists between diff and currSum

            if diff in prefixArr:
                res += prefixArr[diff]

            prefixArr[currSum] = prefixArr.get(currSum, 0) + 1

        return res