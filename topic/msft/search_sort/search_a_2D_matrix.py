from typing import List


# class Solution:
#     flag = False
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
        
#         def find(x, y):
#             if x == y:
#                 if matrix[x][0] == target :
#                     self.flag = True
#                     return x 
#                 return -1
#             if x + 1 == y:
#                 if matrix[x][0] == target or matrix[y][0] == target:
#                     self.flag = True
#                     return
#                 return x
#             mid = (x+y)//2
#             if matrix[mid][0] >= target >= matrix[x][0]:
#                 return find(x, mid)
#             else:
#                 return find(mid, y)
            
#         if matrix[m-1][0] <= target:
#             selected_row = m-1
#         else:
#             selected_row = find(0, m-1)
#         if self.flag:
#             return True


#         def find_col(row, x, y):
#             if x == y:
#                 if matrix[row][x] == target :
#                     self.flag = True
#                     return x 
#                 return -1
#             if x + 1 == y:
#                 if matrix[row][x] == target or matrix[row][y] == target:
#                     self.flag = True
#                     return -1
#                 return -1
#             mid = (x+y)//2
#             if matrix[row][mid] >= target >= matrix[row][x]:
#                 return find_col(row, x, mid)
#             else:
#                 return find_col(row, mid, y)
        
#         print("selected row: ", selected_row)
#         find_col(selected_row, 0, n-1)
#         return self.flag
#           TC: O(log(m) + log(n))
#           SC: O(log(m) + log(n))
    
    
    
class Solution:
    flag = False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        def find(i, j):
            mid = (i+j)//2
            
            first_row = i//n
            first_col = i % n
            
            mid_row = mid // n
            mid_col = mid % n
            
            last_row = j // n
            last_col = j % n
            
            if i == j or i + 1 == j:
                if target == matrix[first_row][first_col] or target == matrix[last_row][last_col] :
                    return True 
                else:
                    return False
            
            val1 = matrix[first_row][first_col]
            val2 = matrix[mid_row][mid_col]
            val3 = matrix[last_row][last_col]
            if val1 <= target <= val2:
                return find(i,mid)
            else:
                return find(mid+1, j)

        return find(0, m*n-1)
    
    
sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13


# matrix = [[1,3],[4,5]]
# target = 5
# matrix = [[1]]
# target = 1


# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
# target = 30 # True
print(sol.searchMatrix(matrix, target))        
            