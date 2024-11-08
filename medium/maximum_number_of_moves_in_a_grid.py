from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        reachable_matrix = [[0]*n for _ in range(m)]
        for i in range(m):
            reachable_matrix[i][0] = 1
        max_moves = 0
        for j in range(1, n):
            flag = False
            for i in range(m):
                if reachable_matrix[i][j-1] and grid[i][j] > grid[i][j-1]:
                    reachable_matrix[i][j] = 1
                if i-1 >= 0 and reachable_matrix[i-1][j-1] and grid[i][j] > grid[i-1][j-1]:
                    reachable_matrix[i][j] = 1
                if i+1 < m and reachable_matrix[i+1][j-1] and grid[i][j] > grid[i+1][j-1]:
                    reachable_matrix[i][j] = 1
                if reachable_matrix[i][j]:
                    flag = True
                
            if flag:
                max_moves = j
            else:
                break
        return max_moves

sol = Solution()
grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid = [[3,2,4],[2,1,9],[1,1,7]]
print(sol.maxMoves(grid))
        
                