class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            remainder = curr_sum % k

            if remainder in prefix_map:
                count += prefix_map[remainder]

            prefix_map[remainder] = prefix_map.get(remainder, 0) + 1

        return count