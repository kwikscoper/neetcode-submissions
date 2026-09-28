class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        #above includes counts for all indices 0 to len(s1) - 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            incomingChar = ord(s2[right]) - ord('a')
            s2Count[incomingChar] += 1
            #if a new character coming is matching
            if s1Count[incomingChar] == s2Count[incomingChar]:
                matches += 1
            #if character that came made it stop matching
            elif s1Count[incomingChar] == s2Count[incomingChar] - 1:
                matches -= 1

            leavingChar = ord(s2[left]) - ord('a')
            s2Count[leavingChar] -= 1
            #if a old character leaving makes it matching
            if s1Count[leavingChar] == s2Count[leavingChar]:
                matches += 1
            #if character that left made it stop matching
            elif s1Count[leavingChar] == s2Count[leavingChar] + 1:
                matches -= 1

            left += 1

        return matches == 26