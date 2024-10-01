class Trie:
    root = dict()
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = {}

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        if '*' in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()

# obj.insert("apple")
# param_2 = obj.search("apple")
# print(param_2)
# param_2 = obj.search("app")
# print(param_2)
# param_3 = obj.startsWith("apb")
# print(param_3)
# obj.insert("app")
# param_2 = obj.search("app")
# print(param_2)

print(obj.startsWith('a'))