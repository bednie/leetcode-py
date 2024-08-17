from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        dq = [(1, beginWord)]
        length = len(beginWord)
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s','t','u','v','w','x','y','z']

        while dq:
            edits, word = dq.pop(0)

            for i in range(length):
                for j in alphabet:
                    candidate = word[:i] + j + word[i+1:]

                    if candidate == endWord:
                        return edits + 1

                    if candidate in words:
                        dq.append((edits + 1, candidate))
                        words.remove(candidate)

        return 0
