from string import ascii_lowercase
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        dq = [(1, beginWord)]
        length = len(beginWord)

        while dq:
            edits, word = dq.pop(0)

            for i in range(length):
                for j in ascii_lowercase:
                    candidate = word[:i] + j + word[i + 1 :]

                    if candidate == endWord:
                        return edits + 1

                    if candidate in words:
                        dq.append((edits + 1, candidate))
                        words.remove(candidate)

        return 0
