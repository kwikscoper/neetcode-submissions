class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        charOrderMap = defaultdict(list)
        indegree = defaultdict(int)
        
        uniqueChars = set()
        for word in words:
            for char in word:
                uniqueChars.add(char)

        firstIdx = 0
        for secondIdx in range(1, len(words)):
            firstWord, secondWord = words[firstIdx], words[secondIdx]
            
            i = 0
            samePrefix = True
            while i < len(firstWord) and i < len(secondWord):
                if firstWord[i] != secondWord[i]:
                    charOrderMap[firstWord[i]].append(secondWord[i])
                    indegree[secondWord[i]] += 1
                    samePrefix = False
                    break

                i += 1

            if samePrefix and len(firstWord) > len(secondWord):
                return ""

            firstIdx += 1

        queue = deque()
        for char in uniqueChars:
            if indegree[char] == 0:
                queue.append(char)

        output = []
        while queue:
            currChar = queue.popleft()
            output.append(currChar)

            for nextChar in charOrderMap[currChar]:
                indegree[nextChar] -= 1
                if indegree[nextChar] == 0:
                    queue.append(nextChar)

        if len(output) != len(uniqueChars):
            return ""

        return "".join(output)


