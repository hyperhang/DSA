from typing import List
import copy
           
             
             
from scipy.optimize import linear_sum_assignment   
import numpy as np         

class Solution:
    INF = 1e6
    def maxScore(self, grid: List[List[int]]) -> int:
        uniq = set()
        updated_grid = []
        for row in grid:
            r = []
            for cell in row:
                uniq.add(100-cell)
                r.append(100-cell)
            updated_grid.append(r)
            
        uniq = list(uniq)
        uniq = sorted(uniq, reverse=True)
        m = len(grid)
        n = len(uniq)
        print("Unique: \n", uniq)
        transformed_grid = [ [self.INF]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if uniq[j] in updated_grid[i]:
                    transformed_grid[i][j] = uniq[j]
        print("Transform grid: ")
        matrix = []
        for i in range(m):
            print(transformed_grid[i])
            matrix.append(np.array(transformed_grid[i]))
        matrix = np.array(matrix)        
        print("matrix: \n", matrix)
        
        row_ind, col_ind = linear_sum_assignment(matrix)
        su = 0
        count = 0
        for i in range(len(row_ind)):
            if matrix[row_ind[i]][col_ind[i]] == self.INF:
                count += 1
            else:
                su += matrix[row_ind[i]][col_ind[i]]
        print("row, col: ", row_ind , col_ind)
        
        
        
        res = 100*(len(row_ind)-count) - su
        print("RES: ", res)
        print("Scipy sum: ", matrix[row_ind,col_ind].sum())
        # print(row_ind, col_ind)
        return int(res)
                
                
            
               
                
class Test():
    def check(self, input, output):
        s = Solution()
        if s.maxScore(input) == output:
            print("Passed!")   
                    
        
      
s = Solution()
grid = [[1,2,3],[4,3,2],[1,1,1]] # 8
# grid = [[8,7,6],[8,3,2]] # 15
# grid = [[5],[7],[19],[5]] #  5 7 19 = 31
grid = [[12,12],[4,4],[12,12]] # 16
grid = [[8,11,3],[17,7,3],[13,20,3],[3,17,20]]  # 61
# grid = [[8,11,3],[17,7,3],         [3,17,20]] # 13
grid = [[16,18],[20,20],[18,18],[1,15]]  # 69

# grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

# grid = [[9, 8,   6, 5],
#         [9, 7,   7 ,6],
#         [8, 5,   4, 2],
#         [7, 6,   5 , 5]
#         ]
grid = [[5],[7],[19],[5]]
grid = [[16,16],[6,16],[16,16],[17,14]]
print(s.maxScore(grid))
