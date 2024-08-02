class WordDictionary:
    def __init__(self):
        self.root = [None] * 27

    def addWord(self, word: str) -> None:
        child = self.root

        for c in word:
            index = ord(c) - 97
            if not child[index]:
                child[index] = [None] * 27
            child = child[index]  

        child[26] = '{'

    def search(self, word: str) -> bool:
        def helper(word: str, children: list):
            if word[0] == '{' and children[-1] == '{': 
                self.res = True
                return
                
            if word[0] == '.':
                for i in children[:26]:
                    if i:
                        helper(word[1:], i)
            else: 
                if children[ord(word[0]) - 97]:
                    helper(word[1:], children[ord(word[0]) - 97])

        self.res = False
        helper(word+'{', self.root)
        return self.res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)