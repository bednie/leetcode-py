from typing import List


class Trie:
        class TrieNode:
            def __init__(self):
                # 26 lowercase English chars, last slot for end of word ('{')
                self.children = [None] * 27

        def __init__(self):
            self.root = [None] * 27

        def insert(self, word: str) -> None:
            children = self.root
            for c in word:
                index = ord(c) - 97
                if not children[index]:
                    children[index] = self.TrieNode().children
                children = children[index]

            children[26] = "{"

        def search(self, word: str) -> bool:
            return self.startsWith(word + "{")

        def startsWith(self, prefix: str) -> bool:
            children = self.root

            for c in prefix:
                index = ord(c) - 97
                if not children[index]:
                    return False
                children = children[index]

            return True
    

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(word: str, seen: list):
            if not word:
                self.result = True
                return

            i,j = seen[-1]

            n = (i-1,j) if i-1 >= 0 else None
            s = (i+1,j) if i+1 < self.m else None
            e = (i,j+1) if j+1 < self.n else None
            w = (i,j-1) if j-1 >= 0 else None

            for c in [n,s,e,w]:
                if c and self.board[c[0]][c[1]] == word[0] and c not in seen:
                    s = seen + [c]
                    dfs(word[1:], s)

            return

        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.result = False
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == word[0]:
                    dfs(word[1:], [(i,j)])

        return self.result

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # sort words in reverse alpha order: apples, apple, app
        # then check trie: if word not in trie, check board with dfs 
        # (use seen and length to search). if word in board, insert into trie so
        # shorter words that share a prefix can be found efficiently.

        # longest possile word is a spiral around the whole board
        # set of seen coords is enough to avoid overlaps and invalid paths.
  
        words = sorted(words, key=len, reverse=True)
        trie = Trie()
        result = []

        for w in words:
            if trie.startsWith(w):
                print(f'{w} exists in trie')
                result.append(w)

            if self.exist(board, w):
                print(f'{w} exists in board')
                trie.insert(w)
                result.append(w)


        print(result) 

        return result
    

