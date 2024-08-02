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
