from typing import List


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        while startPos[0] != homePos[0] or startPos[1] != homePos[1]:
            if startPos[0] < homePos[0]:
                startPos[0] += 1
                cost += rowCosts[startPos[0]]
            elif startPos[0] > homePos[0]:
                startPos[0] -= 1
                cost += rowCosts[startPos[0]]
            print("cost row: ", cost)
            print("new pos: ", startPos)
            if startPos[1] < homePos[1]:
                startPos[1] += 1
                cost += colCosts[startPos[1]]
            elif startPos[1] > homePos[1]:
                startPos[1] -= 1
                cost += colCosts[startPos[1]]
            print("cost col: ", cost)
            print("new pos: ", startPos)
        
        return cost
            
sol = Solution()
startPos = [1, 0]
homePos = [2, 3]
rowCosts = [5, 4, 3]
colCosts = [8, 2, 6, 7]
print(sol.minCost(startPos, homePos, rowCosts, colCosts))