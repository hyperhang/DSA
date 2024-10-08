"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation."""

from typing import List


# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
        
#         def border_rotate(m):
#             leng = n-2*m
#             r, c = m, m
#             if leng == 1:
#                 return
#             for i in range(leng-1):
#                 right = matrix[r+ i][c + leng -1]
#                 matrix[r+ i][c + leng -1] = matrix[r][c+i]
                
#                 bot = matrix[r+leng -1][c + leng - 1 - i]
#                 matrix[r+leng -1][c + leng - 1 - i] = right
                
#                 left = matrix[r+leng -1 -i][c]
#                 matrix[r+leng -1 -i][c] = bot
                
#                 # top
#                 matrix[r][c+i] = left
                
        
#         for i in range(n//2):
#             border_rotate(i)
        
#         return matrix
    
    

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # reverse   
        for j in range(n//2):
            for i in range(n):
                matrix[i][j], matrix[i][n-1 -j] = matrix[i][n-1 -j], matrix[i][j]
        
        return matrix
    
    
    
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(sol.rotate(matrix))
   
                
                
                
