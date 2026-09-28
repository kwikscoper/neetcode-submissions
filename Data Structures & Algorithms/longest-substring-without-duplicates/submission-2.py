class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create map for char -> recently seen index
        seenCharAt = {}
        longest = 0

        #create left pointer
        left = 0
        #right will iterate through the string
        for right, char in enumerate(s):
            #for each char we add to the map
            #if char is in the map, we jump left pointer to 1 past that index
            if char in seenCharAt:
                left = max(left, seenCharAt[char] + 1)
            seenCharAt[char] = right
            #substring length = right - left + 1
            #update longest substring
            longest = max(longest, right - left + 1)

        #return longest
        return longest