class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr: curr[c] = {}
            curr = curr[c]
        curr['*'] = True

    def search(self, word: str) -> bool:
        return self.search_helper(self.root, word)

    def search_helper(self, root: set, word: str) -> bool:
        curr = root
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                recurse = []
                for letter in curr:
                    if letter != '*': recurse.append(self.search_helper(curr[letter], word[i+1:]))
                return any(recurse)
            elif c not in curr: return False
            else: curr = curr[c]
        return '*' in curr

