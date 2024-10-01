from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        grid = dungeon
        m  = len(grid)
        n = len(grid[0])
        dp = [ [0]*n for _ in range(m) ] # init lives
        dp[0][0] = 1 if grid[0][0] >= 0 else -grid[0][0] + 1 
        lives =  [ [0]*n for _ in range(m) ] # current lives
        lives[0][0] = max(1, dp[0][0] + grid[0][0])
        for i in range(1, n):
            t = lives[0][i-1] + grid[0][i]
            dp[0][i] = dp[0][i-1]
            lives[0][i] = t
            if t <= 0:
                dp[0][i] += -t + 1
                lives[0][i] = 1

        for i in range(1, m):
            t = lives[i-1][0] + grid[i][0]
            dp[i][0] = dp[i-1][0]
            lives[i][0] = t
            if t <=0 :
                dp[i][0] += -t + 1
                lives[i][0] = 1
            for j in range(1, n):
                # the left
                l1 =  lives[i][j-1] + grid[i][j]
                t1  = dp[i][j-1]
                
                if l1 <= 0:
                    t1 += -l1 + 1
                    l1 = 1
                
                # above
                l2 = lives[i-1][j] + grid[i][j]
                t2 = dp[i-1][j]
                if l2 <=0:
                    t2 += -l2 + 1
                    l2 = 1
                
                if t1 < t2:
                    dp[i][j] = t1
                    lives[i][j] = l1
                elif t1 > t2:
                    dp[i][j] = t2
                    lives[i][j] = l2
                else:
                    if l1 > l2:
                        dp[i][j] = t1
                        lives[i][j] = l1
                    else:
                        dp[i][j] = t2
                        lives[i][j] = l2
        
        print("dungeon:")
        for i in range(m):
            print(dungeon[i])
        print("------\ninit lives:")        
        for i in range(m):
            print(dp[i])
        print("-----\nCurrent lives:")
        for i in range(m):
            print(lives[i])
        return dp[-1][-1]

s = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]  # 7
dungeon = [[0]]                              # 1
dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]     # 3
print(s.calculateMinimumHP(dungeon))

# # min init lives to reach i,j
# 3, 6, 6
# 8, 16, 6
# 8, 8 , 7

# # current lives
# 1, 1,  4
# 1, 1,  5
# 11, 38, 1


#      -2      1
#     10,6    4
# 10    7      4