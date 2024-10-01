# class Solution:
#     def countSubIslands(self, grid1: list[list], grid2: list[list]) -> int:
#         colors = [ [ 0 for _ in range(len(grid2[0]))] for _ in range (len(grid2))]
#         not_sub_island = set()
        
#         def find_island(row_p, col_p, filled_color = 0):
#             if row_p < 0 or row_p >= len(grid1) or col_p < 0 or col_p >= len(grid1[0]) or colors[row_p][col_p] != 0 or grid2[row_p][col_p] ==0 :
#             # out of idx, or visited, or water
#                 return
#             # not visited, land
#             if grid1[row_p][col_p] != 1:
#                 # grid1 , grid 2 do not have this sub island
#                 not_sub_island.add(filled_color)
                
#             colors[row_p][col_p] = filled_color
#             find_island(row_p-1, col_p, filled_color)
#             find_island(row_p+1, col_p, filled_color)
#             find_island(row_p, col_p-1, filled_color)
#             find_island(row_p, col_p+1, filled_color)
                
#         init_color_num = 0
#         for i in range(len(grid2)):
#             for j in range(len(grid2[0])):
#                 if grid2[i][j] == 1 and colors[i][j] == 0: # land and not visited
#                     init_color_num += 1
#                     print("init color: ", init_color_num)
#                     find_island(i, j, init_color_num)
        
#         print("FULL Color: \n")
#         for r in colors: 
#             print(r)       
#         print("NOT sub island: ")
#         print(not_sub_island)     
#         print("RESULT: ", init_color_num - len(not_sub_island))
#         return init_color_num - len(not_sub_island)
           
           
           
           
class Solution:
    flag = True
    def countSubIslands(self, grid1: list[list], grid2: list[list]) -> int:
        m, n = len(grid1), len(grid1[0])
        def find_island(row_p, col_p):
            if row_p < 0 or row_p >= m or col_p < 0 or col_p >= n or grid2[row_p][col_p] == 0 :
            # out of idx, or visited, or water
                return
            # not visited, land
            if grid1[row_p][col_p] != 1:
                # grid1 , grid 2 do not have this sub island
                self.flag = False
                
            grid2[row_p][col_p] = 0
            find_island(row_p-1, col_p)
            find_island(row_p+1, col_p)
            find_island(row_p, col_p-1)
            find_island(row_p, col_p+1)
                
        count_sub_island = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 : # land (and not visited)
                    find_island(i, j)
                    if self.flag :
                        count_sub_island += 1
                    else:
                        self.flag = True
                        
        return count_sub_island
        

s = Solution()

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
s.countSubIslands(grid1, grid2)

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
s.countSubIslands(grid1, grid2)

grid1 = [[0]]
grid2 = [[1]]
s.countSubIslands(grid1, grid2)