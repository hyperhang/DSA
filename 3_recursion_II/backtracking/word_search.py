from typing import List


class Solution:
    flag = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board), len(board[0])
        def check(i, j):
            visited = [[0]*n for _ in range(m)]
            def dfs(x, y, idx:int):
                if self.flag:
                    return
                
                visited[x][y] = 1
                if board[x][y] == word[idx]:
                    if idx == len(word) - 1:
                        self.flag = True
                        return 
                    if x+1 < m and not visited[x+1][y]:
                        dfs(x + 1, y, idx+1)
                    if x-1>=0 and not visited[x-1][y]:
                        dfs(x - 1, y, idx+1)
                    if y+1 < n and not visited[x][y+1]:
                        dfs(x, y+1, idx+1)
                    if y-1 >=0 and not visited[x][y-1]:
                        dfs(x, y-1, idx+1)
                visited[x][y] = 0
                
            dfs(i, j, 0)
            return
        
        for i in range(m):
            for j in range(n):
                check(i, j)
                if self.flag:
                    return True
        
        return False
        

sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"             
word = "SEE"             
word = "ABCB"             

board = [['a']]
word = 'a'
print(sol.exist(board, word))            