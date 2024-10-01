from typing import List
from operator import add, sub, mul

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        oper = {'+': add, '-': sub, '*': mul}
        def cross_product(l1: list[int], l2:list[int], operator:str) -> list:
            res = []
            for i in l1:
                for j in l2:
                    res.append(oper[operator](i, j))
            return res                
                    
        operators = [ c for c in expression if c in '-+*']
        nums = expression.replace("-", "+").replace("*", "+").split('+')
        num_list = [int(n) for n in nums]
        
        n = len(num_list)
        dp = [[1 for i in range(n+1)] for _ in range(n)]
        # dp[i][j]: tap gia tri cua cac bieu thuc bat dau tai i, co do dai la j
        for i in range(n):
            dp[i][1] = [num_list[i]]
        for j in range(2,n+1):
            for i in range( n+1-j):
                t = []
                for k in range(1, j):
                    x = [dp[i][k]] if type(dp[i][k]) == int else dp[i][k]
                    y = [dp[i+k][j-k]] if type(dp[i+k][j-k]) == int else dp[i+k][j-k]
                    self.count += 1
                    t = t + cross_product(x, y, operators[i+k-1])
                    
                dp[i][j] = t
                
        print(dp[0][n])
        print("length res: ", len(dp[0][n]))
        print("count operators: ", self.count)
        
        return dp[0][n]

s = Solution()
exp = "2*3-4*5"
s.diffWaysToCompute(exp)