from typing import List
import copy

class Trie:
    def __init__(self) -> None:
        self.root = {}
    
    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["*"] = {}
        return
    
          

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        m, n = len(board), len(board[0])
        found_words = set()
        
        def check(i,j):
            visited = [[0]*n for _ in range(m)]
            start = trie.root
            valid_words = []
            def dfs(x:int, y:int, start: str, path: str):
                cur = board[x][y]
                visited[x][y] = 1
                path += cur
                if cur in start:
                    if "*" in start[cur]:
                        valid_words.append(path)
                    if x-1>=0 and not visited[x-1][y]:
                        dfs(x-1, y, start[cur], copy.deepcopy(path))
                    if y+1 < n and not visited[x][y+1]:
                        dfs(x, y+1, start[cur], copy.deepcopy(path))
                    if y-1 >= 0 and not visited[x][y-1]:
                        dfs(x, y-1, start[cur], copy.deepcopy(path))
                    if x+1 < m and not visited[x+1][y]:
                        dfs(x+1, y, start[cur], copy.deepcopy(path))
                
                visited[x][y] = 0
            
            dfs(i, j, trie.root, "")
            return valid_words
        
        
        for i in range(m):
            for j in range(n):
                tem = check(i, j)
                for ele in tem:
                    found_words.add(ele)
        
        return list(found_words)
    
    
sol = Solution()

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# expect: ['oath', 'eat']

board = [["a","b"],["c","d"]]
words = ["abcb"]

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain","hklf", "hf"]
"""
o a b n
o t a e
a h k r
a f l v
words: 
oa
oaa


o a a n
e t a e
i h k r
i f l v
words:
oath, pea, eat, rain, hklf, hf

"""




print(sol.findWords(board, words))

                
         