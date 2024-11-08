from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pivot = 0
        m, n = len(matrix), len(matrix[0])
        while pivot < min(m, n) and target > matrix[pivot][pivot]:
            pivot += 1
        if pivot >= max(m,n):
            return False
        if pivot == min(m, n):
            pivot -= 1
            k = pivot
            while matrix[pivot][k] <= target:
                k += 1
            
        def check(i, j):
            pivot = matrix[i][j]
            while 
            
        