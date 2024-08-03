class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        whole_word = word
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        current.is_end = True
        current.word = whole_word

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]

        return current.is_end


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def search(i: int, j: int, node: TrieNode, length: int):
            if i < 0 or i >= self.m or j < 0 or j >= self.n or length > 10:
                return

            # choose
            c = board[i][j]

            if c not in node.children:
                return

            node = node.children[c]
            if node.is_end:
                self.result.append(node.word)
                node.is_end = False

            # explore
            board[i][j] = None
            for di, dj in self.dirs:
                search(i + di, j + dj, node, length + 1)

            # unchoose
            board[i][j] = c

        self.dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        self.m, self.n = len(board), len(board[0])
        self.result = []
        trie = Trie()

        for word in words:
            trie.insert(word)

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in trie.root.children:
                    search(i, j, trie.root, 0)

        return self.result
