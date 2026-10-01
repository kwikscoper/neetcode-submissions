class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque([beginWord])
        minChanges = 0
        while queue:
            level_len = len(queue)
            for level_item in range(level_len):
                currWord = queue.popleft()
                if currWord == endWord:
                    return minChanges + 1
                
                for i in range(len(currWord)):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = currWord[:i] + letter + currWord[i+1:]
                        if nextWord in wordSet:
                            queue.append(nextWord)
                            wordSet.remove(nextWord)

            minChanges += 1

        return 0